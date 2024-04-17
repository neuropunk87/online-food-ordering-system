class Auth:
    @staticmethod
    def load_login_data():
        try:
            with open("admins.txt", "r") as f:
                admins = [{line.split(",")[0]: line.split(",")[1].strip() for line in f.readlines()}]
        except FileNotFoundError as e:
            admins = []
        try:
            with open("users.txt", "r") as f:
                users = [{line.split(",")[0]: line.split(",")[1].strip() for line in f.readlines()}]
        except FileNotFoundError as e:
            users = []
        return admins, users

    @staticmethod
    def admin_log_in(admins):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        for admin in admins:
            if admin.get(username) == password:
                print("Successfully logged in.")
                return username
        print("Invalid admin credentials. Login failed.")
        return None

    # @staticmethod
    # def admin_sign_up(admins):
    #     username = input("Enter new admin username: ")
    #     for admin in admins:
    #         if admin.get(username):
    #             print(f"Admin '{username}' already exists.")
    #             return None
    #     password = input("Enter new admin password: ")
    #     admins.append({username: password})
    #     print(f"Admin '{username}' successfully registered.")
    #     return username

    @staticmethod
    def user_log_in(users):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in users:
            if user.get(username) == password:
                print("Successfully logged in.")
                return username
        print("Invalid username or password. Login failed.")
        return None

    @staticmethod
    def user_sign_up(users):
        username = input("Enter new username: ")
        for user in users:
            if user.get(username):
                print(f"User '{username}' already exists.")
                return None
        password = input("Enter new password: ")
        users.append({username: password})
        print(f"User '{username}' successfully registered.")
        return username

