from FlaskWebProject4.DAO.GetUsers import getUsers
from FlaskWebProject4.ViewModels.Users import Users
from FlaskWebProject4.Models.User import User

class UsersMB:
    """description of class"""
    def getUsersModel(self):
        users = Users()
        result = getUsers()
        for row in result:
            users.add_user(User(row[0],row[1]))
        return users