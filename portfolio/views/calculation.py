from portfolio import models
from market.api import data

class Asset():

    def __init__(self,models, user_req, pk_req):
        self.query = models.objects
        self.user_req = user_req
        self.pk_req = pk_req

    def creating_query(self):
        queryset = self.query.filter(user_id = self.user_req,id=self.pk_req).values()

        return queryset

    def each_asset(self):
        each_asset = []
        coin = self.creating_query()
        for i in self.query.filter(user_id =self.user_req).values():
            if i['type_id'] == coin[0]['type_id']:
                each_asset.append({
                                   'amount':i['amount'],
                                   'price_paid':i['price_paid'],
                                   'date_created':i['date_created'],
                                   'status':i['status']
                                   })

        return each_asset

    def overal(self):
        overal_of_each_asset = 0
        for i in self.each_asset():
            if i['status'] == 'Buy':
                overal_of_each_asset += i['amount']
            else:
                overal_of_each_asset -= i['amount']

        return overal_of_each_asset

class Portfolio():

    def __init__(self, models, user_req):

        self.query = models.objects
        self.user_req = user_req

    def creating_query(self):
        queryset = self.query.filter(user_id = self.user_req)

        return queryset