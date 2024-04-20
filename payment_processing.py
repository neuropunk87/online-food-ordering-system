from exceptions import InsufficientFundsForPaymentError


class Payment:
    @staticmethod
    def process_payment(total_amount, user):
        order_details = f"Order paid. Total amount: ${total_amount:.2f}\n"
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

