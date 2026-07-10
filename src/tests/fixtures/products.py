import pytest
from decimal import Decimal
from src.api.schemas import ProductUpdate
from src.database.models import Product


@pytest.fixture
def product():
    return Product(id=1, name="Product 1", price=Decimal("100"), stock=100)


@pytest.fixture
def products():
    return [
        Product(id=1, name="Product 1", price=Decimal("100"), stock=100),
        Product(id=2, name="Product 2", price=Decimal("200"), stock=200),
    ]


@pytest.fixture
def product_update():
    return ProductUpdate(
        name="New Product",
        price=Decimal("150"),
        stock=20,
    )
