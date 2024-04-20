import unittest
from user_management import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_view_balance(self):
        self.user.wallet = 100
        self.user.view_balance()
        self.assertEqual(self.user.wallet, 100)

    def test_top_up_wallet(self):
        self.user.top_up_wallet(50)
        self.assertEqual(self.user.wallet, 50)

    def test_save_order_to_history(self):
        order_details = "Order 123 - Burger, Pizza, Pasta"
        User.save_order_to_history(order_details)

        with open("order_history.txt", "r") as file:
            order_details_saved = file.read()
            self.assertEqual(order_details, order_details_saved)


if __name__ == "__main__":
    unittest.main()

