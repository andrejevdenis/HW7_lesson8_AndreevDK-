from itertools import product


class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity


    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if self.check_quantity(quantity) is True:
            self.quantity -= quantity
        else:
            raise ValueError('Не достаточно товара на складе')

    def __hash__(self):
        return hash(self.name + self.description)

class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product not in self.products:
            self.products[product] = buy_count
        else:
            self.products[product] += buy_count


    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products and remove_count is None:
            self.products.pop(product)
        elif product in self.products and remove_count>=self.products[product]:
            self.products.pop(product)
        elif product in self.products and remove_count<self.products[product]:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        return sum (self.products[product] * product.price for product in self.products)

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """

        for Product, quantity in self.products.items():
            Product.buy(quantity)
        self.clear()