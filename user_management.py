class User:
    def __init__(self):
        self.wallet = 0

    def view_balance(self):
        print(f"Wallet Balance: ${self.wallet}")

    def top_up_wallet(self, amount):
        self.wallet += amount
        print(f"Wallet balance topped up. Current balance: ${self.wallet}")

    @staticmethod
    def save_order_to_history(order_details):
        with open("order_history.txt", "a") as file:
            file.write(order_details)

    @staticmethod
    def load_order_history():
        try:
            with open("order_history.txt", "r") as file:
                order_history = file.read()
                print(order_history)
        except FileNotFoundError:
            print("Order history is empty.")

