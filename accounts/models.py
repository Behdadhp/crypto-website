from django.contrib import auth


class User(auth.models.User, auth.models.PermissionsMixin):

    def __init__(self):
        return "@{}".format(self.username)
