from authorization import Auth
from data_storage import Data
from menu_management import Menu
from order_management import Order
from user_management import User
from payment_processing import Payment


print("---> Welcome to the 'Online Food Ordering System' <---")
print("\n---> Menu:")


def main_menu():
    auth = Auth()
    data = Data()
    menu = Menu()
    order = Order()
    user = User()
    payment = Payment()

    admins, users = auth.load_login_data()
    current_user = None
    option = input("Select login option: 1. User\n\t\t\t\t\t 2. Admin\nChoose an option: ")

    while True:
        if option == "1":
            if current_user:
                print(f"\nLogged in as '{current_user}'")
                choice = input("1. View Menu\n"
                               "2. Search for Dishes by Category\n"
                               "3. Search by Dish Name\n"
                               "4. Show Wallet Balance\n"
                               "5. Top Up Balance\n"                               
                               "6. Add Dish to Cart\n"
                               "7. Remove Dish from Cart\n"
                               "8. Make Order\n"                               
                               "9. Pay Online\n"
                               "10. Check Order Status\n"
                               "11. Order History\n"
                               "12. Log Out\n"
                               "0. Exit\n"
                               "Choose an option: ")
                if choice == "1":
                    menu.load_menu_data()
                elif choice == "2":
                    search_dish_category = input("Enter dish category to search for: ")
                    menu.find_dish_by_category(search_dish_category)
                elif choice == "3":
                    search_dish_name = input("Enter dish name to search for: ")
                    menu.find_dish_by_name(search_dish_name)
                elif choice == "4":
                    user.view_balance()
                elif choice == "5":
                    amount = float(input("Enter the amount to top up the wallet: "))
                    user.top_up_wallet(amount)
                elif choice == "6":
                    dish_name = input("Enter dish name to add to the cart: ")
                    quantity = int(input("Enter the quantity: "))
                    order.add_dish_to_cart(dish_name, quantity)
                elif choice == "7":
                    dish_name = input("Enter dish name to remove from the cart: ")
                    order.remove_dish_from_cart(dish_name)
                elif choice == "8":
                    order.make_order()
                elif choice == "9":
                    payment.process_payment(order.total_amount, user)
                elif choice == "10":
                    order.check_order_status()
                elif choice == "11":
                    user.load_order_history()
                elif choice == "12":
                    current_user = None
                    print("Logged out successfully.")
                elif choice == "0":
                    break
            else:
                choice = input("1. Log In\n"
                               "2. Sign Up\n"
                               "3. View Menu\n"
                               "4. Search for Dishes by Category\n"
                               "5. Search by Dish Name\n"
                               "0. Exit\n"
                               "Choose an option: ")
                if choice == "1":
                    current_user = auth.user_log_in(users)
                elif choice == "2":
                    current_user = auth.user_sign_up(users)
                    data.save_credentials(admins, users)
                elif choice == "3":
                    print("Welcome, guest!")
                    menu.load_menu_data()
                elif choice == "4":
                    search_dish_category = input("Enter dish category to search for: ")
                    menu.find_dish_by_category(search_dish_category)
                elif choice == "5":
                    search_dish_name = input("Enter dish name to search for: ")
                    menu.find_dish_by_name(search_dish_name)
                elif choice == "0":
                    break
        elif option == "2":
            if current_user:
                print(f"\nLogged in as '{current_user}'")
                choice = input("1. Show List of Dishes\n"
                               "2. Add Dish in Menu\n"
                               "3. Edit Dish Price\n"
                               "4. Remove Dish from Menu\n"
                               "5. Log out\n"
                               "0. Exit.\n"
                               "Choose an option: ")
                if choice == "1":
                    menu.load_menu_data()
                elif choice == "2":
                    new_dish_name = input("Enter new dish name: ")
                    dish_category = input("Enter dish category: ")
                    dish_price = float(input("Enter price of dish: "))
                    menu.add_dish(new_dish_name, dish_category, dish_price)
                elif choice == "3":
                    dish_name = input("Enter dish name for edit: ")
                    new_price = float(input("Enter new price of dish: "))
                    menu.edit_dish(dish_name, new_price)
                elif choice == "4":
                    dish_name = input("Enter dish name for remove: ")
                    menu.remove_dish(dish_name)
                elif choice == "5":
                    current_user = None
                    print("Logged out successfully.")
                elif choice == "0":
                    break
            else:
                choice = input("1. Log In\n"
                               # "2. Sign Up\n"
                               "0. Exit\n"
                               "Choose an option: ")
                if choice == "1":
                    current_user = auth.admin_log_in(admins)
                # elif choice == "2":
                    # current_user = auth.admin_sign_up(admins)
                    # data.save_credentials(admins, users)
                elif choice == "0":
                    break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()

