import pytest

from src.shopflow.shop import (
    Category,
    Product,
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
    new_product = Product(
        '55" QLED 4K',
        "Фоновая подсветка",
        123000.0,
        7,
        "Черный",
    )
    shop_category.add_product(new_product)
    assert Category.product_count == count_before + 1


def test_invalid_class_instance(shop_category):
    with pytest.raises(
        TypeError,
        match="Товар не является экземпляром класса Product",
    ):
        shop_category.add_product("invalid_instance")


def test_string_representation_category(
    shop_category,
):
    assert str(shop_category) == f"{shop_category.name}, количество продуктов: 14 шт."


# ============ CLASS PRODUCT ============


def test_init_product(shop_product):
    assert shop_product.name == "Xiaomi Redmi Note 11"
    assert shop_product.description == "1024GB, Синий"
    assert shop_product.price == 31000.0
    assert shop_product.quantity == 14
    assert shop_product.color == "Синий"


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
        "color": "Серый",
    }

    new_prod = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
            "color": "Серый",
        }
    )

    assert new_prod.name == mirror["name"]
    assert new_prod.description == mirror["description"]
    assert new_prod.price == mirror["price"]
    assert new_prod.quantity == mirror["quantity"]
    assert new_prod.color == mirror["color"]


def test_string_representation_prod(shop_product):
    assert str(shop_product) == f"{shop_product.name}, {shop_product.price} руб. Остаток: {shop_product.quantity} шт."


def test_calculates_the_price_amount():
    prod_1 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        10,
        2,
        "Синий",
    )
    prod_2 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        5,
        3,
        "Синий",
    )
    result = prod_1 + prod_2
    assert result == 35


def test_cannot_add_products_of_different_types(shop_product, shop_laws):
    with pytest.raises(TypeError):
        assert shop_product + shop_laws


# ============ CLASS SMARTPHONE ============


def test_smartphone_initialization(shop_smart):
    assert shop_smart.efficiency == 95.5
    assert shop_smart.model == "Model X"
    assert shop_smart.memory == 256
    assert shop_smart.color == "Черный"


# ============ CLASS LAWNGRASS ============


def test_lawn_grass_initialization(shop_laws):
    assert shop_laws.country == "Россия"
    assert shop_laws.germination_period == "7 дней"
    assert shop_laws.color == "Зеленый"
