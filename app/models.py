from sqlalchemy import  Column, ForeignKey, Integer, String, Table, Identity, select
from sqlalchemy.orm import relationship

from manager import ConnManager

Base = ConnManager(echo=True).Base

product_category = Table(
    "product_category",
    Base.metadata,
    Column("product_pk", ForeignKey("product_table.id")),
    Column("category_pk", ForeignKey("category_table.id")),
)


class Product(Base):
    __tablename__ = "product_table"
    id = Column(Integer, Identity(always=True), primary_key=True, index=True, autoincrement=True)
    value = Column(String)
    
    categories = relationship(
        "Category", secondary=product_category, back_populates="products"
    )


class Category(Base):
    __tablename__ = "category_table"
    id = Column(Integer, Identity(always=True), primary_key=True, index=True, autoincrement=True)
    value = Column(String)
    
    products = relationship(
        "Product", secondary=product_category, back_populates="categories"
    )