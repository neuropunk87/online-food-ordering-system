class Data:
    @staticmethod
    def save_credentials(admins, users):
        with open("admins.txt", "w") as f:
            for admin in admins:
                for login, password in admin.items():
                    f.write(f"{login},{password}\n")
        with open("users.txt", "w") as f:
            for user in users:
                for login, password in user.items():
                    f.write(f"{login},{password}\n")

