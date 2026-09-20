import pytest
import pytest
from shopping_cart import ShoppingCart


@pytest.fixture
def default_item():
    return {"name": "Apple", "price": 15.5, "quantity": 2}


@pytest.fixture
def cart_with_item(default_item):
    cart = ShoppingCart()
    cart.add_item(
        name=default_item["name"],
        price=default_item["price"],
        quantity=default_item["quantity"]
    )
    return cart


class TestShoppingCart:
    def test_init(self):
        cart = ShoppingCart()
        assert cart.items == []

    def test_add_new_item(self, default_item):
        cart = ShoppingCart()
        cart.add_item(default_item["name"], default_item["price"], default_item["quantity"])
        assert len(cart.items) == 1
        assert cart.items[0] == default_item

    def test_add_existing_item_updates_quantity_and_price(self, cart_with_item):
        cart_with_item.add_item("Apple", 18.0, 3)
        assert len(cart_with_item.items) == 1
        assert cart_with_item.items[0]["quantity"] == 5
        assert cart_with_item.items[0]["price"] == 18.0

    def test_remove_item(self, cart_with_item):
        cart_with_item.add_item("Banana", 10.0, 5)
        cart_with_item.remove_item("Apple")
        assert len(cart_with_item.items) == 1
        assert cart_with_item.items[0]["name"] == "Banana"

    def test_remove_non_existent_item(self, cart_with_item):
        cart_with_item.remove_item("Orange")
        assert len(cart_with_item.items) == 1

    def test_get_total(self, cart_with_item):
        cart_with_item.add_item("Banana", 10.0, 3) # + 30.0
        assert cart_with_item.get_total() == 61.0