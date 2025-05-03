
class UserAuth:
    def __init__(self):
        self.users = {"admin": "admin123", "user": "user123"}

    def login(self, username: str, password: str) -> bool:
        return self.users.get(username) == password
