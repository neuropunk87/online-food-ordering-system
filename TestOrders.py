import unittest
from unittest import mock
from order_management import Order
from exceptions import UnavailableForOrderError


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order = Order()

    def test_add_dish_to_cart(self):
        self.order.add_dish_to_cart("Burger", 1)
        self.assertEqual(len(self.order.cart), 1)
        self.assertEqual(self.order.cart[0]["dish_name"], "Burger")
        self.assertEqual(self.order.cart[0]["quantity"], 1)

    def test_add_dish_to_cart_invalid_dish(self):
        with self.assertRaises(UnavailableForOrderError):
            self.order.add_dish_to_cart("Invalid", 1)

    def test_remove_dish_from_cart(self):
        self.order.add_dish_to_cart("Burger", 1)
        self.order.add_dish_to_cart("Pizza", 2)
        self.order.remove_dish_from_cart("Burger")
        self.assertEqual(len(self.order.cart), 1)
        self.assertEqual(self.order.cart[0]["dish_name"], "Pizza")
        self.assertEqual(self.order.cart[0]["quantity"], 2)

    def test_make_order(self):
        with mock.patch("builtins.input", return_value="y"):
            self.order.add_dish_to_cart("Burger", 1)
            self.order.add_dish_to_cart("Pizza", 2)
            self.order.make_order()
            self.assertEqual(self.order.total_amount, 23.97)

    def test_check_order_status(self):
        self.order.status = "Delivered"
        status = self.order.check_order_status()
        self.assertEqual(status, "Delivered")


if __name__ == "__main__":
    unittest.main()

