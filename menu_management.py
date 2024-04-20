class Dish:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price


class Menu:
    def __init__(self):
        self.dishes = []

    @staticmethod
    def load_menu_data():
        with open("menu_data.txt", "r") as file:
            for line in file.readlines():
                name, category, price = line.strip().split(", ")
                dish = Dish(name, category, price)
                print(f"Name: {dish.name}, Category: {dish.category}, Price: {dish.price}")

    def save_menu_data(self):
        with open("menu_data.txt", "a") as file:
            for dish in self.dishes:
                file.write(f"{dish.name}, {dish.category}, {dish.price}\n")

    def add_dish(self, name, category, price):
        new_dish = Dish(name, category, price)
        self.dishes.append(new_dish)
        self.save_menu_data()
        print(f"New dish added to menu.\nName: {name}, Category: {category}, Price: {price}")

    @staticmethod
    def edit_dish(dish_name, new_price):
        temp_dishes = []
        found_dish = False
        with open("menu_data.txt", "r") as file:
            for line in file:
                name, category, price = line.strip().split(", ")
                if name == dish_name:
                    found_dish = True
                    temp_dishes.append(f"{name}, {category}, {new_price}\n")
                else:
                    temp_dishes.append(f"{name}, {category}, {price}\n")

        if not found_dish:
            print("Dish not found.")
            return

        with open("menu_data.txt", "w") as file:
            for dish_info in temp_dishes:
                file.write(dish_info)
        print("Dish price updated.")

    @staticmethod
    def remove_dish(dish_name):
        temp_dishes = []
        found_dish = False
        with open("menu_data.txt", "r") as file:
            for line in file:
                name, category, price = line.strip().split(", ")
                if name == dish_name:
                    found_dish = True
                else:
                    temp_dishes.append(f"{name}, {category}, {price}\n")

        if not found_dish:
            print("Dish not found.")
            return

        with open("menu_data.txt", "w") as file:
            for dish_info in temp_dishes:
                file.write(dish_info)
        print("Dish removed.")

    @staticmethod
    def find_dish_by_category(category):
        found_dishes = []
        with open("menu_data.txt", "r") as file:
            category_found = False
            for line in file:
                name, dish_category, price = line.strip().split(", ")
                if dish_category.lower() == category.lower():
                    found_dishes.append(f"Name: {name}, Category: {dish_category}, Price: {price}")
                    category_found = True
            if category_found:
                for dish in found_dishes:
                    print(dish)
            else:
                print("Category not found.")
        return found_dishes

    @staticmethod
    def find_dish_by_name(dish_name):
        with open("menu_data.txt", "r") as file:
            for line in file:
                name, category, price = line.strip().split(", ")
                if name.lower() == dish_name.lower():
                    print(f"Name: {name}, Category: {category}, Price: {price}")
                    return f"Name: {name}, Category: {category}, Price: {price}"
        print("Dish not found.")

