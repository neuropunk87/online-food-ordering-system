class InsufficientFundsForPaymentError(Exception):
    def __init__(self, message="Insufficient funds for payment. Payment processing failed."):
        self.message = message
        super().__init__(self.message)


class Payment:
    @staticmethod
    def process_payment(total_amount, user):
        order_details = f"Total amount of your paid order: ${total_amount:.2f}\n"
        confirmation = input(f"Confirm payment of ${total_amount} (Y/N): ")
        if confirmation.lower() == "y":
            if user.wallet >= total_amount:
                user.wallet -= total_amount
                user.save_order_to_history(order_details)
                print("Payment processed successfully.")
                print("Remaining balance: $", user.wallet)
            else:
                raise InsufficientFundsForPaymentError()
        else:
            print("Order canceled.")

