"""This module contains the User class"""
class User(object):
    """This class describes the structure of the User object"""

    shopping_lists = {}

    def __init__(self, username, password, first_name, last_name):
        """This method creates an instance of the User class"""
        pass

    def change_password(self, new_password):
        """This method changes the password of the User instance"""
        pass

    def create_shopping_list(self, shopping_list):
        """This method creates a shopping list in the User instance"""
        pass

    def remove_shopping_list(self, shopping_list):
        """This method removes a shopping list from the User instance"""
        pass

    def edit_shopping_list(self, old_title, new_title):
        """This method changes the title of a shopping list in the User instance"""
        pass
