from src.shopflow.shop import Category, Product


def setup_function():
    # Сбрасываем счётчики перед каждым тестом для изоляции
    Category.category_count = 0
    Category.product_count = 0


def test_product_creation_and_attributes():
    p = Product("Товар", "Описание", 199.99, 10)
    assert p.name == "Товар"
    assert p.description == "Описание"
    assert isinstance(p.price, float)
    assert p.price == 199.99
    assert p.quantity == 10


def test_product_with_integer_price_and_zero_quantity():
    p = Product("Штука", "Без количества", 100, 0)
    assert isinstance(p.price, int)
    assert p.quantity == 0


def test_category_counters_and_products_length():
    p1 = Product("A", "a", 10, 1)
    p2 = Product("B", "b", 20, 2)

    assert Category.category_count == 0
    assert Category.product_count == 0

    Category("Cat1", "desc1", [p1, p2])  # просто создаём объект
    assert Category.category_count == 1
    assert Category.product_count == 2

    Category("Cat2", "desc2", [])  # просто создаём объект
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_with_empty_name_and_long_description():
    # Проверяем, что пустые/длинные строки корректно сохраняются
    long_desc = "x" * 2000
    c = Category("", long_desc, [])
    assert c.name == ""
    assert c.description == long_desc


def test_mutating_products_list_reflects_in_category():
    p1 = Product("X", "x", 1, 1)
    products = [p1]
    c = Category("C", "d", products)
    # добавляем продукт во внешнюю коллекцию — категория должна ссылаться на тот же список
    p2 = Product("Y", "y", 2, 2)
    products.append(p2)
    assert len(c.products) == 2


def test_module_main_executes_and_prints(capsys):
    import runpy

    # Выполнить модуль как скрипт — это должно выполнить блок if __name__ == '__main__'
    runpy.run_module('src.shopflow.shop', run_name="__main__")

    captured = capsys.readouterr()
    out = captured.out

    # Ожидаем, что в выводе есть имена продуктов и названия категорий и итоговые счётчики
    assert 'Samsung Galaxy S23 Ultra' in out
    assert 'Iphone 15' in out
    assert 'Телевизоры' in out
    # после создания двух категорий общий счётчик категорий должен быть напечатан (2)
    assert '\n2\n' in out or ' 2\n' in out
    # общее число продуктов во всех категориях — 4
    assert '\n4\n' in out or ' 4\n' in out
