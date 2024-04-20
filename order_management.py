from exceptions import UnavailableForOrderError


class Order:
    def __init__(self):
        self.dish_name = ""
        self.quantity = 0
        self.cart = []
        self.total_amount = 0
        self.status = "In Progress"

    def add_dish_to_cart(self, dish_name, quantity):
        with open("menu_data.txt", "r") as file:
            menu_data = file.readlines()
            found = False
            for line in menu_data:
                item = line.strip().split(", ")
                if dish_name.lower() == item[0].lower():
                    self.cart.append({"dish_name": item[0], "price": float(item[2]), "quantity": quantity})
                    found = True
                    print(f"{quantity} {dish_name}(s) added to cart.")
                    break

            if not found:
                raise UnavailableForOrderError()

    def remove_dish_from_cart(self, dish_name):
        for item in self.cart:
            if item["dish_name"].lower() == dish_name.lower():
                self.cart.remove(item)
                print(f"{dish_name} removed from cart.")

    def make_order(self):
        self.total_amount = sum([item["price"] * item["quantity"] for item in self.cart])
        print("Order Summary:")
        for item in self.cart:
            print(f"{item['quantity']} x {item['dish_name']} - ${item['price']} each")
        print(f"Total Amount: ${self.total_amount}")

        confirmation = input("Confirm order (Y/N): ")
        if confirmation.lower() == "y":
            self.status = "Order Placed"
            print("Order placed successfully. Please proceed to Online Payment.")
        else:
            print("Order canceled.")

    def check_order_status(self):
        self.status = "Delivered"
        print(f"Order status: {self.status}")
        return self.status

