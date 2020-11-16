from FlaskWebProject4.Models.User import User

class Users:
    def __init__(self):
        self.user_list = list()

    def add_user(self,user):
        self.user_list.append(user)