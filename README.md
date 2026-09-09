# ShopFlow

Примерная модель магазина с классами для продуктов и категорий, демонстрационными данными, проверкой бизнес-правил и тестами.

---

## 1. Описание проекта

`ShopFlow` — небольшой пример проекта на Python, демонстрирующий простые доменные модели магазина:

- Класс `Product` — модель товара с полями `name`, `description`, `price`, `quantity` и `color`.
- Класс `Category` — категория товаров, хранящая список продуктов и поддерживающая счётчики:
	- `Category.category_count` — общее число созданных категорий.
	- `Category.product_count` — суммарное число продуктов во всех категориях.
- Класс `Smartphone` — наследник `Product` с характеристиками эффективности, модели и объёма памяти.
- Класс `LawnGrass` — наследник `Product` с характеристиками страны происхождения и срока прорастания.

В текущей реализации `Product` дополнительно включает:
- валидацию цены через property `price` — цена должна быть строго больше нуля;
- фабричный метод `new_product()` для создания товара из словаря;
- строковое представление через `__str__()` с названием, ценой и остатком на складе;
- сложение товаров через `__add__()` — суммирование их полных стоимостей (`цена * количество`);
- автоматическое обновление счётчиков и проверку типа товара при добавлении в категорию.

Класс `Category` также реализует `__str__()`: он возвращает название категории и
суммарное количество единиц товара в ней.

Проект включает демонстрационный блок `if __name__ == "__main__":` в `src/shopflow/shop.py` (печатает примерные данные), а также тесты в `tests/test_shop.py`.

---

## 2. Технологии и стек

- Язык: Python 3.12
- Тестирование: `pytest`
- Покрытие: `pytest-cov`
- Линтинг/анализ: `ruff`, `mypy`, `flake8`
- Формат проекта: пакет в `src/` (модульный импорт как `src.shopflow.*`)

В runtime-зависимостях проекта нет сторонних библиотек — используется только стандартная библиотека Python. Основные инструменты разработки и проверки устанавливаются через Poetry-группы `dev` и `lint`.

---

## 3. Инструкция по установке

1. Клонировать репозиторий:
```bash
git clone git@github.com:SergeyRomanov9896/ShopFlow.git
cd ShopFlow
```

2. (Опционально) Создать и активировать виртуальное окружение:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Unix / macOS
source .venv/bin/activate
```

---

## 4. Установить зависимости

После клонирования проекта зависимости устанавливаются одной командой:
```bash
poetry install
```

Эта команда устанавливает:
- `pytest` и `pytest-cov` для тестов;
- `ruff`, `mypy` и `flake8` для проверки качества кода;
- проектный пакет `shopflow` из каталога `src`.

> Новых runtime-зависимостей в проекте не появилось: внешние библиотеки для бизнес-логики не используются.

---

## 5. Как запустить проект

- Запуск демо-скрипта (выполняет блок `if __name__ == "__main__"` и выводит примеры):
```bash
python -m src.shopflow.shop
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

## 6. Примеры использования

Примеры основаны на коде в `src/shopflow/shop.py`.

1) Создание продукта и проверка цены:
```python
from src.shopflow.shop import Product

p = Product("Телефон", "Смартфон, 128GB", 29999.0, 5, "Черный")
print(p.name)         # Телефон
print(p.price)        # 29999.0
print(p.quantity)     # 5

p.price = -40
# Цена не должна быть нулевая или отрицательная
print(p.price)        # 29999.0
```

2) Создание продукта из словаря через `new_product()`:
```python
from src.shopflow.shop import Product

product_data = {
    "name": "Samsung Galaxy S23 Ultra",
    "description": "256GB, Серый цвет, 200MP камера",
    "price": 180000.0,
    "quantity": 5,
    "color": "Серый",
}

new_product = Product.new_product(product_data)
print(new_product.name)        # Samsung Galaxy S23 Ultra
print(new_product.description) # 256GB, Серый цвет, 200MP камера
print(new_product.price)       # 180000.0
print(new_product.color)       # Серый
```

3) Строковое представление продукта и категории:
```python
from src.shopflow.shop import Category, Product

product = Product("Телефон", "Смартфон, 128GB", 29999.0, 5, "Черный")
print(str(product))
# Телефон, 29999.0 руб. Остаток: 5 шт.

category = Category("Смартфоны", "Мобильные устройства", [product])
print(str(category))
# Смартфоны, количество продуктов: 5 шт.
```

4) Сложение полных стоимостей товаров через `__add__()`:
```python
from src.shopflow.shop import Product

phone = Product("Телефон", "Смартфон", 29999.0, 2, "Черный")
case = Product("Чехол", "Защитный чехол", 999.0, 3, "Прозрачный")

total = phone + case
print(total)  # 62995.0
```

5) Создание категории и добавление товара:
```python
from src.shopflow.shop import Product, Category

p1 = Product("A", "a", 100, 1, "Черный")
p2 = Product("B", "b", 200, 2, "Белый")

category = Category("Смартфоны", "Мобильные устройства", [p1, p2])
print(Category.category_count)  # 1 или больше, если категории уже создавались
print(Category.product_count)   # 2 или больше, если товары добавлялись в другие категории

product3 = Product("C", "c", 300, 3, "Серый")
category.add_product(product3)
print(Category.product_count)   # увеличился на 1
```

6) Попытка добавить в категорию значение неверного типа:
```python
try:
    category.add_product("не товар")
except TypeError as error:
    print(error)  # Товар не является экземпляром класса Product
```

7) Использование специализированных товаров:
```python
from src.shopflow.shop import LawnGrass, Smartphone

smartphone = Smartphone(
    "Телефон", "Флагманский смартфон", 100000.0, 2,
    95.5, "Model X", 256, "Черный"
)
grass = LawnGrass(
    "Газонная трава", "Для дачного участка", 500.0, 20,
    "Россия", "7 дней", "Зеленый"
)

print(smartphone.model, smartphone.memory)  # Model X 256
print(grass.country, grass.germination_period)  # Россия 7 дней
```

8) Покрытие блока запуска как скрипта:
```bash
python -m src.shopflow.shop
# Выводит примеры продуктов и итоговые счётчики
```

---

## 7. Тесты и покрытие

Тесты находятся в `tests/test_shop.py` и проверяют:
- корректную инициализацию `Product` и его поля `color`,
- обновление счётчиков `Category` при создании категорий,
- корректную работу `Product.new_product()` при передаче словаря,
- строковое представление `Product` и `Category` через `__str__()`,
- расчёт общей стоимости товаров через `Product.__add__()`,
- запрет сложения товаров разных типов,
- корректную инициализацию `Smartphone` и `LawnGrass`,
- валидацию цены при нулевых и отрицательных значениях,
- добавление корректного товара в категорию и увеличение счётчика,
- отказ при передаче объекта, не являющегося экземпляром `Product`,
- выполнение демонстрационного блока через запуск модуля как `__main__`.

Запуск тестов:
```bash
pytest --cov=src.shopflow --cov-report=term-missing -q
```
