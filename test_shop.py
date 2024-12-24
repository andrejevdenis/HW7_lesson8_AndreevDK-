"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart

@pytest.fixture
def product():
    return Product("book", 1000, "Flowers for Algernon", 100)

@pytest.fixture
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(100) is True
        assert product.check_quantity(product.quantity) is True
        assert product.check_quantity(product.quantity + 1) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(100) != ValueError

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1000)

class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):
        cart.add_product(product=product, buy_count=2)
        cart.add_product(product=product, buy_count=2)
        assert cart.products[product] == 4

    def test_remove_product(self, cart, product):
        cart.add_product(product=product, buy_count=5)
        cart.remove_product(product=product, remove_count=2)
        assert cart.products[product] == 3
        cart.add_product(product=product, buy_count=5)
        cart.remove_product(product=product, remove_count=10)
        assert cart.products == {}
        cart.add_product(product=product, buy_count=5)
        cart.remove_product(product=product)
        assert cart.products == {}
        cart.add_product(product=product, buy_count=5)
        cart.remove_product(product=product, remove_count=5)
        assert cart.products == {}

    def test_clear(self, cart, product):
        cart.add_product(product=product, buy_count=5)
        cart.clear()
        assert cart.products == {}

    def test_total_price(self, cart, product):
        cart.add_product(product=product, buy_count=3)
        cart.add_product(product=product, buy_count=3)
        cart.get_total_price()
        assert cart.get_total_price() == 6000

    def test_buy(self, cart, product):
        cart.add_product(product=product, buy_count=10)
        cart.buy()
        assert cart.products == {}
        cart.add_product(product=product, buy_count=1000)
        with pytest.raises(ValueError):
            cart.buy()