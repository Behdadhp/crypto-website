from market.api import data
from decimal import Decimal


class Query:

    def __init__(self, model, user, pk=None):
        self.model = model.objects
        self.user = user
        self.pk = pk

    def create_detail_query_portfolio(self):
        return self.model.filter(user_id=self.user, id=self.pk).values()

    def create_list_query_portfolio(self):
        return self.model.filter(user_id=self.user)


class Asset(Query):

    def each_asset(self):
        each_asset = []
        coin = self.create_detail_query_portfolio()
        for i in self.model.filter(user_id=self.user).values():
            if i['type_id'] == coin[0]['type_id']:
                each_asset.append({
                    'amount': i['amount'],
                    'price_paid': i['price_paid'],
                    'date_created': i['date_created'],
                    'status': i['status']
                })

        return each_asset

    def overall(self):
        overall_of_each_asset = 0
        for i in self.each_asset():
            if i['status'] == 'Buy':
                overall_of_each_asset += i['amount']
            else:
                overall_of_each_asset -= i['amount']

        return overall_of_each_asset


class Portfolio(Query):

    def creating_portfolio_lst(self):
        portfolio_list = []
        for item in self.create_list_query_portfolio():
            portfolio_list.append({
                'type': item.type.coin,
                'amount': item.amount,
                'status': item.status,
                'id': item.id
            })

        return portfolio_list

    def creating_set_of_assets(self):
        set_of_assets = set()
        for item in self.creating_portfolio_lst():
            set_of_assets.add(item['type'])
        return list(set_of_assets)

    def getting_current_price(self, coin_type):
        for item in data:
            if item['name'] == coin_type:
                return item['current_price']
            else:
                pass

    def total_amount_of_asset(self, coin_type):
        amount_of_asset = 0
        for item in self.creating_portfolio_lst():
            if item['type'] == coin_type and item['status'] == 'Buy':
                amount_of_asset += item['amount']
            elif item['type'] == coin_type and item['status'] == 'Sell':
                amount_of_asset -= item['amount']

        return amount_of_asset

    def getting_coin_id(self, coin_type):
        for item in self.creating_portfolio_lst():
            if item['type'] == coin_type:
                return item['id']

    def creating_portfolio_dict(self, coin_type):
        total_amount = self.total_amount_of_asset(coin_type)
        current_price = self.getting_current_price(coin_type)
        coin_id = self.getting_coin_id(coin_type)
        portfolio_dict = {
            'name': coin_type,
            'asset': round(total_amount, 5),
            'current_price': current_price if total_amount >= 0 else 'Negative',
            'value': '{:.2f}'.format(total_amount * current_price) if total_amount >= 0 else 'Error',
            'id': coin_id
        }

        return portfolio_dict

    def run(self):
        asset_list = []
        for item in self.creating_set_of_assets():
            asset_list.append(self.creating_portfolio_dict(item))
        return asset_list
