from abc import ABC, abstractmethod
from typing import ClassVar


class CreationInfoMixin:
    def __init__(self, *args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{key}={repr(value)}" for key, value in kwargs.items()]
        all_args = ", ".join(args_repr + kwargs_repr)
        print(f"{self.__class__.__name__}({all_args})")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов магазина.

    Атрибуты:
        name (str): Название товара.
        description (str): Краткое описание товара.
        price (int | float): Цена товара (должна быть > 0).
        quantity (int): Количество товара на складе.
        color (str): Цвет товара.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int,
        color: str = "Белый",
    ) -> None:
        """Инициализирует общие атрибуты продукта."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.color = color
        super().__init__()

    @property
    def price(self) -> float | int:
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float | int) -> None:
        """Сеттер для установки цены с проверкой."""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового представления продукта."""
        pass


class Product(CreationInfoMixin, BaseProduct):
    """Модель продукта магазина.

    Наследует все атрибуты от BaseProduct.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float | int,
        quantity: int,
        color: str = "Белый",
    ) -> None:
        super().__init__(name, description, price, quantity, color)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]
        color = product_data["color"]

        return cls(name, description, price, quantity, color)

    def __add__(self, other) -> int | float:
        """Возвращает сумму полных стоимостей двух товаров на складе (цена * количество)."""
        if type(self) is not type(other):
            raise TypeError("Нельзя сложить объекты разных типов")
        self_total = self.price * self.quantity
        other_total = other.price * other.quantity
        return self_total + other_total


class Category:
    """Категория товаров.

    Хранит список продуктов и поддерживает два класса-счётчика:
    `category_count` — общее число созданных категорий,
    `product_count` — суммарное число продуктов во всех созданных категориях.
    """

    name: str
    description: str
    __products: list[Product]

    category_count: ClassVar[int] = 0
    product_count: ClassVar[int] = 0

    def __init__(self, name, description, products) -> None:
        """Инициализация категории и обновление счётчиков.

        Аргументы:
            name: название категории.
            description: описание категории.
            products: список объектов `Product` принадлежащих категории.
        """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self) -> str:
        result = []

        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(result)

    def add_product(self, product: Product) -> None:
        if issubclass(type(product), Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Товар не является экземпляром класса Product")


class Smartphone(Product):
    """Модель смартфона, расширяющая базовые свойства продукта.

    Атрибуты:
        efficiency (float): Эффективность смартфона.
        model (str): Модель смартфона.
        memory (int): Объём памяти в гигабайтах.
    """

    efficiency: float
    model: str
    memory: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует смартфон.

        Аргументы:
            name: название товара.
            description: описание смартфона.
            price: цена смартфона.
            quantity: доступное количество.
            efficiency: эффективность смартфона.
            model: модель смартфона.
            memory: объём памяти в гигабайтах.
            color: цвет смартфона.
        """
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory


class LawnGrass(Product):
    """Модель газонной травы, расширяющая базовые свойства продукта.

    Атрибуты:
        country (str): Страна происхождения семян.
        germination_period (str): Срок прорастания.
    """

    country: str
    germination_period: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует газонную траву.

        Аргументы:
            name: название товара.
            description: описание газонной травы.
            price: цена газонной травы.
            quantity: доступное количество.
            country: страна происхождения семян.
            germination_period: срок прорастания.
            color: цвет газонной травы.
        """
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
    )

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
