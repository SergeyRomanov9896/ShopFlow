# ShopFlow

Учебный проект на Python для моделирования интернет-магазина: продукты, категории, специализированные товары и проверка бизнес-правил.

---

## 1. Описание проекта

`ShopFlow` — пример объектной модели магазина с базовыми сущностями и проверками корректности данных.

### Основные сущности

- `CreationInfoMixin` — миксин, который печатает имя класса и аргументы конструктора при создании объекта.
- `BaseProduct` — абстрактный базовый класс для всех товаров.
- `Product` — базовый товар с полями `name`, `description`, `price`, `quantity` и `color`.
- `Category` — категория товаров, хранит список продуктов и поддерживает счётчики:
  - `Category.category_count` — число созданных категорий;
  - `Category.product_count` — суммарное число товаров во всех категориях.
- `Smartphone` — наследник `Product`, добавляющий `efficiency`, `model`, `memory` и `color`.
- `LawnGrass` — наследник `Product`, добавляющий `country`, `germination_period` и `color`.

### Что реализовано в текущей версии

`Product` поддерживает:

- проверку количества: при `quantity == 0` выбрасывается `ValueError`;
- проверку цены через property `price`: значение должно быть больше нуля, иначе выводится сообщение в консоль;
- фабричный метод `new_product()` для создания продукта из словаря;
- строковое представление через `__str__()`;
- сложение товаров через `__add__()` по формуле `цена * количество`;
- запрет сложения объектов разных типов с `TypeError`;
- создание объекта через `CreationInfoMixin`.

`Category` поддерживает:

- строковое представление через `__str__()`;
- свойство `products`, возвращающее строку со всеми товарами в категории;
- метод `add_product()`, который добавляет товар только если он является наследником `Product`;
- расчёт средней цены товаров через `middle_price()`; для пустой категории возвращается `0`.

Демонстрационный сценарий находится в `main.py`, а тесты — в `tests/test_shop.py`.

---

## 2. Технологии и стек

- Язык: Python 3.12
- Тестирование: `pytest`
- Покрытие: `pytest-cov`
- Линтинг и анализ: `ruff`, `mypy`, `flake8`
- Структура проекта: пакет в `src/` с импортом вида `from shopflow.shop import ...`

Проект использует только стандартную библиотеку Python; инструменты разработки устанавливаются через Poetry.

---

## 3. Установка

1. Клонировать репозиторий:

```bash
git clone https://github.com/SergeyRomanov9896/ShopFlow.git
cd ShopFlow
```

2. Создать и активировать виртуальное окружение (по желанию):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Unix / macOS
source .venv/bin/activate
```

3. Установить зависимости:

```bash
poetry install
```

---

## 4. Как запустить проект

- Запуск демо-скрипта:

```bash
python main.py
```

- Запуск тестов:

```bash
pytest -q
```

- Запуск тестов с отчётом по покрытию:

```bash
pytest --cov=src.shopflow --cov-report=term-missing -q
```

---

## 5. Примеры использования

### 5.1. Создание и проверка товара

```python
from shopflow.shop import Product

p = Product("Телефон", "Смартфон, 128GB", 29999.0, 5, "Черный")
print(p.name)      # Телефон
print(p.price)     # 29999.0
print(p.quantity)  # 5

p.price = -40
print(p.price)     # Цена не должна быть нулевая или отрицательная
```

> Важно: при попытке установить цену `<= 0` значение не меняется, а в консоль выводится предупреждение.

### 5.2. Создание товара из словаря

```python
from shopflow.shop import Product

product_data = {
    "name": "Samsung Galaxy S23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5,
    "color": "Серый",
}

new_product = Product.new_product(product_data)
print(new_product.name)      # Samsung Galaxy S23 Ultra
print(new_product.price)     # 180000.0
print(new_product.color)     # Серый
```

### 5.3. Строковое представление товара и категории

```python
from shopflow.shop import Category, Product

product = Product("Телефон", "Смартфон, 128GB", 29999.0, 5, "Черный")
print(str(product))
# Телефон, 29999.0 руб. Остаток: 5 шт.

category = Category("Смартфоны", "Мобильные устройства", [product])
print(str(category))
# Смартфоны, количество продуктов: 5 шт.
```

### 5.4. Сложение товаров

```python
from shopflow.shop import Product

phone = Product("Телефон", "Смартфон", 29999.0, 2, "Черный")
case = Product("Чехол", "Защитный чехол", 999.0, 3, "Прозрачный")

total = phone + case
print(total)  # 62995.0
```

### 5.5. Добавление товара в категорию

```python
from shopflow.shop import Category, Product

p1 = Product("A", "a", 100, 1, "Черный")
p2 = Product("B", "b", 200, 2, "Белый")
category = Category("Смартфоны", "Мобильные устройства", [p1, p2])

product3 = Product("C", "c", 300, 3, "Серый")
category.add_product(product3)
print(Category.product_count)
```

### 5.6. Ошибка при неверном типе товара

```python
from shopflow.shop import Category

category = Category("Смартфоны", "Мобильные устройства", [])

try:
    category.add_product("не товар")
except TypeError as error:
    print(error)
    # Товар не является экземпляром класса Product
```

### 5.7. Нулевая цена и нулевое количество

```python
from shopflow.shop import Product

try:
    Product("Бракованный товар", "Неверное количество", 1000.0, 0)
except ValueError as error:
    print(error)
    # Товар с нулевым количеством не может быть добавлен
```

### 5.8. Специализированные товары

```python
from shopflow.shop import LawnGrass, Smartphone

smartphone = Smartphone(
    "Телефон",
    "Флагманский смартфон",
    100000.0,
    2,
    95.5,
    "Model X",
    256,
    "Черный",
)

grass = LawnGrass(
    "Газонная трава",
    "Для дачного участка",
    500.0,
    20,
    "Россия",
    "7 дней",
    "Зеленый",
)

print(smartphone.model, smartphone.memory)  # Model X 256
print(grass.country, grass.germination_period)  # Россия 7 дней
```

### 5.9. Средняя цена товаров в категории

```python
from shopflow.shop import Category, Product

p1 = Product("A", "a", 100, 1, "Черный")
p2 = Product("B", "b", 200, 2, "Белый")
category = Category("Категория", "Описание", [p1, p2])

print(category.middle_price())  # 150.0
```

---

## 6. Тесты и покрытие

Тесты находятся в `tests/test_shop.py` и проверяют:

- корректную инициализацию `Product` и его полей;
- обновление счётчиков `Category`;
- корректную работу `Product.new_product()`;
- строковое представление через `__str__()`;
- сумму стоимости товаров через `__add__()`;
- запрет сложения товаров разных типов;
- инициализацию `Smartphone` и `LawnGrass`;
- валидацию цены при нулевых и отрицательных значениях;
- валидацию `quantity == 0` при создании товара;
- добавление корректного товара в категорию;
- выброс `TypeError` при попытке передать объект неверного типа;
- расчёт средней цены товаров в категории через `middle_price()`;
- вывод информации о создании объекта через `CreationInfoMixin`.

Команда запуска:

```bash
pytest --cov=src.shopflow --cov-report=term-missing -q
```

---

## 7. Структура репозитория

```text
ShopFlow/
├── main.py
├── pyproject.toml
├── README.md
├── src/
│   └── shopflow/
│       ├── __init__.py
│       └── shop.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_shop.py
├── htmlcov/
└── .pytest_cache/
```

