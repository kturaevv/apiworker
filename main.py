from fastapi import FastApi, Depends
from sqlalchemy.orm import Session

from app.models import models, engine, Session
from app.manager import ConnManager
from app.crud import CRUD

# Dependency
def get_db():
    db = ConnManager().session
    try:
        yield db
    finally:
        db.close()

app = FastApi()

@app.get('/products')
def get_products(db: Session = Depends(get_db)):
    ...

@app.get('/categories')
def get_categories(db: Session = Depends(get_db)):
    ...

@app.get('/both')
def get_products_and_categories(db: Session = Depends(get_db)):
    ...
