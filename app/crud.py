from sqlalchemy import select

from manager import ConnManager
from models import Product, Category


class CRUD(ConnManager):
    """ Convenience class, all methods bundled toghether for simplified unit tests and API usage."""

    def __init__(self) -> None:
        super().__init__()
                
    def _fake_populate_products_categories(
            self, 
            n_products: int = 30, 
            categories: list[str] = ['A', 'B', 'C', 'D']
        ) -> None:
        from faker import Faker
                
        faker = Faker()

        products = [Product(value=faker.catch_phrase()) for _ in range(n_products)]
        categories = [Category(value=category) for category in categories]

        self.session.bulk_save_objects(products + categories) # deprecated
        self.session.commit()

    def get_products(self) -> list[Product]:
        result = self.session.execute(select(Product))
        return result.scalars().all()

    def get_categories(self) -> list[Category]:
        result = self.session.execute(select(Category))
        return result.scalars().all()

    def get_products_and_categories(self):
        ...
