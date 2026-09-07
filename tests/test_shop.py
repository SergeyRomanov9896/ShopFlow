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


# ============ CLASS CATEGORY ============


def test_init_category(shop_category, shop_product):
    assert shop_category.name == "Смартфоны"
    assert (
        shop_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    products_str = shop_category.products

    assert isinstance(products_str, str)

    expected_str = f"{shop_product.name}, {shop_product.price} руб. Остаток: {shop_product.quantity} шт."
    assert products_str == expected_str


def test_adding_categories(shop_category):
    count_before = Category.product_count
    new_product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    shop_category.add_product(new_product)
    assert Category.product_count == count_before + 1


def test_invalid_class_instance(shop_category, capsys):
    shop_category.add_product("invalid_instance")
    readut = capsys.readouterr()
    assert readut.out.strip() == "Товар не является экземпляром класса Product"

    def test_string_representation_categor(shop_category):
        assert str(shop_category) == f"{shop_category.name}, количество продуктов: {shop_category.product_count} шт."


# ============ CLASS PRODUCT ============


def test_init_product(shop_product):
    assert shop_product.name == "Xiaomi Redmi Note 11"
    assert shop_product.description == "1024GB, Синий"
    assert shop_product.price == 31000.0
    assert shop_product.quantity == 14


@pytest.mark.parametrize("negative", [0, -1])
def test_negative_price_value(capsys, shop_product, negative):
    shop_product.price = negative
    readut = capsys.readouterr()
    assert readut.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_positive_price_value(shop_product):
    new_prod = shop_product.price = 5000
    assert new_prod == 5000


def test_correctness_dictionary_unpacking():

    mirror = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }

    new_prod = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )

    assert new_prod.name == mirror["name"]
    assert new_prod.description == mirror["description"]
    assert new_prod.price == mirror["price"]
    assert new_prod.quantity == mirror["quantity"]


def test_string_representation_prod(shop_product):
    assert str(shop_product) == f"{shop_product.name}, {shop_product.price} руб. Остаток: {shop_product.quantity} шт."


def test_calculates_the_price_amount():
    prod_1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 10, 2)
    prod_2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 5, 3)
    result = prod_1 + prod_2
    assert result == 35
