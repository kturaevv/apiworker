from fastapi import FastAPI

from app.manager import ConnManager
from app.crud import CRUD
from app import schemas

app = FastAPI()
crud = CRUD()

@app.on_event("startup")
def startup():
    ConnManager().define_tables()
    crud._fake_populate_products_categories()
    crud._fake_populate_junction_table()
    print("STARTUP")

@app.on_event("shutdown")
def shutdown():
    ConnManager().drop_tables()
    print("SHUTDOWN")

@app.get('/products', response_model=list[schemas.Product])
def get_products_and_its_categories():
    return crud.get_products()

@app.get('/categories', response_model=list[schemas.Category])
def get_categories_and_its_products():
    return crud.get_categories()

@app.get('/both', response_model=list[schemas.ProductCategory])
def get_product_category_pairs():
    return crud.get_products_and_categories()
