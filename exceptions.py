class UnavailableForOrderError(Exception):
    def __init__(self, message="This dish is not available to order. Please choose something else."):
        self.message = message
        super().__init__(self.message)


class InsufficientFundsForPaymentError(Exception):
    def __init__(self, message="Insufficient funds for payment. Payment processing failed."):
        self.message = message
        super().__init__(self.message)

