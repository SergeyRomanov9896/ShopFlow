from typing import ClassVar


class Product:
    """Модель продукта магазина.

    Атрибуты:
        name (str): Название товара.
        description (str): Краткое описание товара.
        quantity (int): Количество товара на складе.
    """

    name: str
    description: str
    quantity: int
    color: str

    def __init__(self, name: str, description: str, price: int | float, quantity: int, color: str) -> None:
        """Инициализирует экземпляр `Product`.

        Аргументы:
            name: название товара.
            description: описание товара.
            price: цена (целая или дробная)
            quantity: доступное количество.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.color = color

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> int | float:
        return self.__price

    @price.setter
    def price(self, new_price: int | float) -> None:
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

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

    category_count: ClassVar[int] = 0
    product_count: ClassVar[int] = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
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
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
