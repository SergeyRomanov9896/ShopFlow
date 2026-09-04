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

    def __init__(self, name: str, description: str, price: int | float, quantity: int) -> None:
        """Инициализирует экземпляр `Product`.

        Аргументы:
            name: название товара
            description: описание товара
            price: цена (целая или дробная)
            quantity: доступное количество
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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

        return cls(name, description, price, quantity)

    def __add__(self, other) -> int | float:
        """Возвращает сумму полных стоимостей двух товаров на складе (цена * количество)."""
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
            name: название категории
            description: описание категории
            products: список объектов `Product` принадлежащих категории
        """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        return f"{self.description}, количество продуктов: {self.product_count} шт."

    @property
    def products(self) -> str:
        result = []

        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(result)

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Товар не является экземпляром класса Product")


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
