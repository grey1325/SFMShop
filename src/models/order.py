from typing import List

from src.models.exceptions import InvalidOrderError, BusinessLogicError
from src.models.product import Product
from src.models.user import User


class Order:
    def __init__(self, user: User, products: List[Product]):
        self.user = user
        if not products:
            raise BusinessLogicError("Заказ невалиден: пустой список товаров")
        self.products = products


    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_total_price()
        return total

    def product_search(self, product):
        try:
            if product not in self.products:
                raise KeyError("Товар не найден")
        except KeyError as e:
            print(f"Ошибка: {e}")
        else:
            return "Товар найден"

    def add_product(self, product):
        if not isinstance(product, Product):
            raise InvalidOrderError("Невалидный товар")
        self.products.append(product)

    def __str__(self):
        return f"Заказ пользователя {self.user.name} на сумму {self.calculate_total()}"



