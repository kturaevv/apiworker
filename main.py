from fastapi import FastApi, Depends
from sqlalchemy.orm import Session
from app.models import models, engine, Session

# Dependency
def get_db():
    db = Session()
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
