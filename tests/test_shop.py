import pytest

from src.shopflow.shop import Category, Product


@pytest.fixture()
def shop_product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def shop_category(shop_product):
    return Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни""",
        [shop_product],
    )


def test_init_product(shop_product):
    assert shop_product.name == "Xiaomi Redmi Note 11"
    assert shop_product.description == "1024GB, Синий"
    assert shop_product.price == 31000.0
    assert shop_product.quantity == 14


def test_init_category(shop_category, shop_product):
    assert shop_category.name == "Смартфоны"
    assert (
        shop_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(shop_category.products) == 1

    product_in_category = shop_category.products[0]
    assert product_in_category.name == shop_product.name
    assert product_in_category.description == shop_product.description
    assert product_in_category.price == shop_product.price
    assert product_in_category.quantity == shop_product.quantity


def test_category_counters():
    # Сбрасываем счетчики перед тестом для чистоты эксперимента
    Category.category_count = 0
    Category.product_count = 0

    p1 = Product("Товар 1", "Описание 1", 100.0, 1)
    p2 = Product("Товар 2", "Описание 2", 200.0, 2)

    # Создаем категорию с двумя товарами
    Category("Тестовая категория", "Описание", [p1, p2])

    # Проверяем, что счетчики корректно увеличились
    assert Category.category_count == 1
    assert Category.product_count == 2
