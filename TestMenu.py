import unittest
from menu_management import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.test_menu_data = "Burger, Fast Food, 5.99\nPizza, Italian, 8.99\nSushi, Japanese, 12.99\n"
        with open("menu_data.txt", "w") as file:
            file.write(self.test_menu_data)

    def test_load_menu_data(self):
        Menu.load_menu_data()
        with open("menu_data.txt", "r") as file:
            loaded_data = file.read()
        self.assertEqual(loaded_data, self.test_menu_data)

    def test_add_menu_data(self):
        menu = Menu()
        menu.add_dish("Steak", "Main Course", 19.99)
        self.assertEqual(len(menu.dishes), 1)

    def test_save_menu_data(self):
        menu = Menu()
        menu.save_menu_data()
        self.assertNotEqual(menu.dishes, self.test_menu_data)

    def test_edit_dish(self):
        dish_name = "Burger"
        new_price = 6.99
        Menu.edit_dish(dish_name, new_price)
        with open("menu_data.txt", "r") as file:
            for line in file:
                name, category, price = line.strip().split(", ")
                if name == dish_name:
                    self.assertEqual(float(price), new_price)
                    return

    def test_remove_dish(self):
        dish_name = "Pizza"
        Menu.remove_dish(dish_name)
        with open("menu_data.txt", "r") as file:
            for line in file:
                name, category, price = line.strip().split(", ")
                self.assertNotEqual(name, dish_name)

    def test_find_dish_by_category(self):
        test_menu_data = "Burger, Fast Food, 5.99\nPizza, Italian, 8.99\nSushi, Japanese, 12.99\n"
        with open("menu_data.txt", "w") as file:
            file.write(test_menu_data)

        found_dishes = Menu.find_dish_by_category("Italian")
        self.assertEqual(len(found_dishes), 1)
        self.assertEqual(found_dishes[0], "Name: Pizza, Category: Italian, Price: 8.99")

    def test_find_dish_by_name_existing_dish(self):
        with open("menu_data.txt", "w") as file:
            file.write("Soup, Starter, 5.99\n")
            file.write("Salad, Starter, 7.99\n")

        expected_output = "Name: Soup, Category: Starter, Price: 5.99"
        actual_output = Menu.find_dish_by_name("soup")
        self.assertEqual(actual_output, expected_output)

    def test_find_dish_by_name_non_existing_dish(self):
        with open("menu_data.txt", "w") as file:
            file.write("Salad, Starter, 7.99\n")

        actual_output = Menu.find_dish_by_name("Pizza")
        self.assertIsNone(actual_output)


if __name__ == "__main__":
    unittest.main()

