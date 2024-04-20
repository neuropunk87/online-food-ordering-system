import unittest
from exceptions import UnavailableForOrderError, InsufficientFundsForPaymentError


class TestCustomExceptions(unittest.TestCase):
    def test_unavailable_for_order_error(self):
        with self.assertRaises(UnavailableForOrderError) as context:
            raise UnavailableForOrderError()
        self.assertEqual(str(context.exception), "This dish is not available to order. Please choose something else.")

    def test_insufficient_funds_for_payment_error(self):
        with self.assertRaises(InsufficientFundsForPaymentError) as context:
            raise InsufficientFundsForPaymentError()
        self.assertEqual(str(context.exception), "Insufficient funds for payment. Payment processing failed.")


if __name__ == "__main__":
    unittest.main()

