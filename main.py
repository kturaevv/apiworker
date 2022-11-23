from fastapi import FastAPI

from app import schemas, config
from app.crud import CRUD
from app.manager import ConnManager

from celery import Celery

app = FastAPI()
crud = CRUD()
settings = config.get_settings()

celery = Celery(
    'tasks', 
    backend='rpc://', 
    broker=f'pyamqp://{settings.rabbitmq_host}:{settings.rabbitmq_port}',
    task_cls='worker.tasks:BaseTask'
    )


@app.on_event("startup")
def startup():
    ConnManager().drop_tables_if_exist()
    ConnManager().define_tables()
    crud._fake_populate_products_categories()
    crud._fake_populate_junction_table()


@app.on_event("shutdown")
def shutdown():
    ConnManager().drop_tables()


@app.get('/products', response_model=list[schemas.Product])
def get_products_and_its_categories():
    return crud.get_products()


@app.get('/categories', response_model=list[schemas.Category])
def get_categories_and_its_products():
    return crud.get_categories()


@app.get('/both', response_model=list[schemas.ProductCategory])
def get_product_category_pairs():
    return crud.get_products_and_categories()

@app.get("/heavy/")
def heavy_api_call(q: int = 1):
    celery.send_task(
        'test', (q,)
    )
    return "Success"