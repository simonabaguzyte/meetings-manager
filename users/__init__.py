class User:
    def __init__(self, username):
        self.username = username


    # pavercia useri i dictionary (duomenu struktura)
    def to_dict(self):
        return {"username": self.username}


    def __str__(self):
        return f"<User username={self.username}>"
