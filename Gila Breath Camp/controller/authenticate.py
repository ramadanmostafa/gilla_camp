from database.database_functions import *

class AuthUser(object):
    """used in the authentication process"""

    def __init__(self, username, password):
        self.__username__ = username
        self.__password__ = password

    def authenticate(self):
        result = select_username_password(self.__username__, self.__password__)
        return result != None

    def is_admin(self):
        result = select_username_password(self.__username__, self.__password__)
        return result[0] == 1
