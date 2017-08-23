"""This module contains the core functionality methods of the Shopping List application"""
from app.models.item import Item
from app.models.shopping_list import ShoppingList
from app.models.user import User


class ShoppingListApplication(object):
    """This This class describes the structure of the ShoppingListApplication object"""

    def __init__(self):
        self.users = {}
        self.logged_in = {}
        self.sharing_pool = {}

    def login(self, email, password):
        """This method enables stored users to login"""
        self.logged_in[email] = False
        if self.users and email in self.users.keys():
            user = self.users[email]
            if user.password == password:
                self.logged_in[user.email] = True
        return self.logged_in[email]

    def logout(self, email):
        """This method enables stored users to logout"""
        if email in self.logged_in.keys():
            self.logged_in[email] = False
        return self.logged_in[email]

    def signup(self, email, password):
        """This method enables new users to create accounts"""
        if email in self.users.keys():
            return None
        new_user = User(
            email=email,
            password=password,
            shopping_lists={}
        )
        self.users[new_user.email] = new_user
        self.logged_in[new_user.email] = True
        return self.users[new_user.email]

    def create_shopping_list(self, title, email):
        """This method enables logged in users to create new shopping lists"""
        if email in self.logged_in.keys() and self.logged_in[email]:
            title = title.replace("'", "`").replace('"', '``')
            new_shopping_list = ShoppingList(title, {})
            user = self.users[email]
            return user.create_shopping_list(new_shopping_list)
        return None

    def edit_shopping_list(self, old_title, new_title, email):
        """This method enables logged in users to edit their shopping lists"""
        if email in self.logged_in.keys() and self.logged_in[email]:
            new_title = new_title.replace("'", "`").replace('"', '``')
            user = self.users[email]
            return user.edit_shopping_list(old_title, new_title).title == new_title
        return None

    def remove_shopping_list(self, title, email):
        """This method enables logged in users to edit their shopping lists"""
        if email in self.logged_in.keys() and self.logged_in[email]:
            user = self.users[email]
            if title in user.shopping_lists.keys():
                shopping_list = user.shopping_lists[title]
                return user.remove_shopping_list(shopping_list)
        return None

    def share_shopping_list(self, title, email):
        """This method enables logged in users to share their shopping lists"""
        if email in self.logged_in.keys() and self.logged_in[email]:
            user = self.users[email]
            if title in user.shopping_lists.keys():
                not_existing = True
                if user.email in self.sharing_pool.keys():
                    if title in self.sharing_pool[user.email].keys():
                        not_existing = False
                if not_existing:
                    self.sharing_pool[user.email] = {
                        title: user.shopping_lists[title]}
                    return True
        return False

    def add_item(self, name, list_title, price, email):
        """This method enables logged in users to add items to their shopping lists"""
        if email in self.logged_in.keys() and self.logged_in[email]:
            user = self.users[email]
            if list_title in user.shopping_lists.keys():
                shopping_list1 = user.shopping_lists[list_title]
                name = name.replace("'", "`").replace('"', '``')
                if name not in shopping_list1.items.keys():
                    new_item = Item(name, price)
                    return shopping_list1.add_item(new_item)
        return None

    def edit_item(self, list_title, old_name, new_name, new_price, email):
        """This method enables logged in users to add items to their shopping lists"""
        if email in self.logged_in.keys() and self.logged_in[email]:
            user = self.users[email]
            if list_title in user.shopping_lists.keys():
                shopping_list2 = user.shopping_lists[list_title]
                if old_name in shopping_list2.items.keys():
                    item = shopping_list2.items[old_name]
                    new_name = new_name.replace("'", "`").replace('"', '``')
                    item.rename(new_name)
                    item.change_price(new_price)
                    shopping_list2.items[new_name] = item
                    if not old_name == new_name:
                        del shopping_list2.items[old_name]
                    return item.name == new_name and item.price == new_price
        return False

    def remove_item(self, list_title, name, email):
        """This method enables logged in users to remove items from their shopping lists"""
        if email in self.logged_in.keys() and self.logged_in[email]:
            user = self.users[email]
            if list_title in user.shopping_lists.keys():
                shopping_list3 = user.shopping_lists[list_title]
                if name in shopping_list3.items.keys():
                    item1 = shopping_list3.items[name]
                    return shopping_list3.remove_item(item1)
        return None

    def check_item_toggle(self, list_title, name, new_status, email):
        """This method enables logged in users to check and uncheck items on their shopping lists"""
        if email in self.logged_in.keys() and self.logged_in[email]:
            user = self.users[email]
            if list_title in user.shopping_lists.keys():
                shopping_list4 = user.shopping_lists[list_title]
                if name in shopping_list4.items.keys():
                    item2 = shopping_list4.items[name]
                    return item2.change_status(new_status)
        return None

    def get_all_lists(self, email):
        """This method gets all the shopping lists for a user"""
        if email in self.logged_in.keys() and self.logged_in[email] and email in self.users.keys():
            user = self.users[email]
            if self.sharing_pool:
                for share_email, shopping_list_dict in self.sharing_pool.items():
                    if not share_email == user.email:
                        for title, shared_shopping_list in shopping_list_dict.items():
                            if title not in user.shopping_lists.keys():
                                user.shopping_lists[title] = shared_shopping_list
                                break
            return user.shopping_lists
        return {}
