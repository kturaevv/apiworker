from sqlalchemy import  Column, ForeignKey, Integer, String, Table, Identity, select
from sqlalchemy.orm import relationship

from .manager import ConnManager

Base = ConnManager().Base

class ProductCategory(Base):
    __tablename__ = "product_category"
    id = Column(Integer, primary_key=True)
    product_pk = Column(ForeignKey("product_table.id"))
    category_pk = Column(ForeignKey("category_table.id"))

    products = relationship("Product", back_populates="categories")
    categories = relationship("Category", back_populates="products")


class Product(Base):
    __tablename__ = "product_table"
    id = Column(Integer, Identity(always=True), primary_key=True, index=True, autoincrement=True)
    value = Column(String)
    
    categories = relationship(
        "ProductCategory", back_populates="products"
    )


class Category(Base):
    __tablename__ = "category_table"
    id = Column(Integer, Identity(always=True), primary_key=True, index=True, autoincrement=True)
    value = Column(String)
    
    products = relationship(
        "ProductCategory", back_populates="categories"
    )
