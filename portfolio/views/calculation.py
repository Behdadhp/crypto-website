from market.api import data


class Asset():

    def __init__(self, models, user_req, pk_req):
        self.query = models.objects
        self.user_req = user_req
        self.pk_req = pk_req

    def creating_query(self):
        queryset = self.query.filter(user_id=self.user_req, id=self.pk_req).values()

        return queryset

    def each_asset(self):
        each_asset = []
        coin = self.creating_query()
        for i in self.query.filter(user_id=self.user_req).values():
            if i['type_id'] == coin[0]['type_id']:
                each_asset.append({
                    'amount': i['amount'],
                    'price_paid': i['price_paid'],
                    'date_created': i['date_created'],
                    'status': i['status']
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
        queryset = self.query.filter(user_id=self.user_req)

        return queryset

    def creating_portfolio_lst(self):
        portfolio_list = []
        for item in self.creating_query():
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
        portfolio_dict = {}
        total_amount = self.total_amount_of_asset(coin_type)
        current_price = self.getting_current_price(coin_type)
        coin_id = self.getting_coin_id(coin_type)
        if total_amount >= 0:
            portfolio_dict = {
                'name': coin_type,
                'asset': total_amount,
                'current_price': current_price,
                'value': '{:.2f}'.format(total_amount * current_price),
                'id': coin_id
            }
        else:
            portfolio_dict = {
                'name': coin_type,
                'asset': 'Negativ',
                'current_price': current_price,
                'value': 'Error',
                'id': coin_id
            }

        return portfolio_dict

    def run(self):
        asset_list = []
        for item in self.creating_set_of_assets():
            asset_list.append(self.creating_portfolio_dict(item))
        return asset_list
