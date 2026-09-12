import pytest

from shopflow.shop import (
    Category,
    LawnGrass,
    Product,
    Smartphone,
)


@pytest.fixture()
def shop_product():
    return Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        "Синий",
    )


@pytest.fixture()
def shop_category(shop_product):
    return Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни""",
        [shop_product],
    )


@pytest.fixture()
def shop_smart():
    return Smartphone(
        "Телефон",
        "Описание",
        1000.0,
        2,
        95.5,
        "Model X",
        256,
        "Черный",
    )


@pytest.fixture()
def shop_laws():
    return LawnGrass(
        "Трава",
        "Описание",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
