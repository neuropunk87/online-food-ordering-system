import unittest
import unittest.mock
from payment_processing import Payment
from exceptions import InsufficientFundsForPaymentError
from user_management import User


class TestPayment(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.wallet = 100

    def test_process_payment_sufficient_funds(self):
        mock_input = lambda _: "y"
        with unittest.mock.patch("builtins.input", mock_input):
            total_amount = 50
            Payment.process_payment(total_amount, self.user)
            self.assertEqual(self.user.wallet, 50)

    def test_process_payment_insufficient_funds(self):
        mock_input = lambda _: "y"
        with unittest.mock.patch("builtins.input", mock_input):
            total_amount = 150
            with self.assertRaises(InsufficientFundsForPaymentError):
                Payment.process_payment(total_amount, self.user)

    def test_process_payment_order_cancel(self):
        mock_input = lambda _: "n"
        with unittest.mock.patch("builtins.input", mock_input):
            total_amount = 50
            Payment.process_payment(total_amount, self.user)
            self.assertEqual(self.user.wallet, 100)


if __name__ == "__main__":
    unittest.main()

