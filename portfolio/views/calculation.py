from portfolio import models
from market.api import data

class Asset():

    def __init__(self,models, user_req, pk_req):
        self.query = models.objects
        self.user_req = user_req
        self.pk_req = pk_req