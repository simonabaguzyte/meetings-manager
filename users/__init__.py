class User:
    def __init__(self, username):
        self.username = username
    
    @classmethod
    def from_raw(cls, dict):
        return cls(username=dict["username"])
    
    def to_dict(self):
        return {"username": self.username}
    
    def __str__(self):
        return f"<User username={self.username}>"