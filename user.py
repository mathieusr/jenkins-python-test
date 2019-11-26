
class User:

    def __init__(self, email:str, first_name:str = "", last_name:str = "", age:int = None):

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def is_valid(self):

        if "@"  in self.email and self.first_name and self.last_name and self.age > 13:

            return True

        return False