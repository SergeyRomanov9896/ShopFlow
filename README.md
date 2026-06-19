# ShopFlow

Примерная модель магазина с классами для продуктов и категорий, демонстрационными данными и тестами.

---

## 1. Описание проекта

`ShopFlow` — небольшой пример проекта на Python, демонстрирующий простые доменные модели магазина:

- Класс `Product` — модель товара с полями `name`, `description`, `price`, `quantity`.
- Класс `Category` — категория товаров, хранящая список продуктов и поддерживающая счётчики:
	- `Category.category_count` — общее число созданных категорий.
	- `Category.product_count` — суммарное число продуктов во всех категориях.

Проект включает демонстрационный блок `if __name__ == "__main__":` в `src/shopflow/shop.py` (печатает примерные данные) и тесты в `tests/test_shop.py`.

---

## 2. Технологии и стек

- Язык: Python 3.10+ (рекомендуется Python 3.12)
- Тестирование: `pytest`
- Формат проекта: пакет в `src/` (модульный импорт как `src.shopflow.*`)

Код не зависит от сторонних библиотек — только стандартная библиотека Python, поэтому установка минимальна.

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

## 4. Установить зависимостей:
```
poetry install
```

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

---

## 6. Примеры использования

Примеры основаны на коде в `src/shopflow/shop.py`.

1) Создание продукта и чтение атрибутов:
```python
from src.shopflow.shop import Product

p = Product("Телефон", "Смартфон, 128GB", 29999.0, 5)
print(p.name)         # Телефон
print(p.price)        # 29999.0
print(p.quantity)     # 5
```

2) Создание категории и обновление глобальных счётчиков:
```python
from src.shopflow.shop import Product, Category

p1 = Product("A", "a", 100, 1)
p2 = Product("B", "b", 200, 2)

print(Category.category_count, Category.product_count)  # 0 0

c = Category("Смартфоны", "Мобильные устройства", [p1, p2])

print(Category.category_count)  # 1
print(Category.product_count)   # 2
```

3) Покрытие блока запуска как скрипта:
```bash
python -m src.shopflow.shop
# Выводит примеры продуктов и итоговые счётчики
```

---

## 7. Тесты и покрытие

Тесты находятся в `tests/test_shop.py` и проверяют:
- корректную инициализацию `Product` (включая int/float для цены и нулевое количество),
- обновление счётчиков `Category` при создании категорий,
- поведение при изменении списка продуктов из внешнего контекста,
- выполнение демо-блока через запуск модуля как `__main__`.

Запуск тестов:
```bash
pytest --cov=src.shopflow --cov-report=term-missing -q
```
