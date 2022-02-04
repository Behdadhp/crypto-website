from django.shortcuts import render
from django.views import generic
from portfolio import models
from market.models import Market
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePortfolio
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()
from market.api import data
from accounts.models import User
from django.contrib.auth.decorators import login_required







class PortfolioList(generic.ListView , LoginRequiredMixin):
    context_object_name = 'portfolio_lists'
    queryset = models.Portfolio.objects.all().order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset_portfolio = models.Portfolio.objects.filter(user_id = self.request.user)


#  Total Asset of each coin:
        portfolioList = total_assets(queryset_portfolio)
        context['asset']= portfolioList

        return context






class PortfolioCreate(LoginRequiredMixin,generic.CreateView):
    model = models.Portfolio
    form_class = CreatePortfolio


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PortfolioDetail(generic.DetailView,LoginRequiredMixin):
    context_object_name = 'portfolio_details'
    model = models.Portfolio
    template_name = 'portfolio/portfolio_detail.html'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset_portfolio_user = models.Portfolio.objects.filter(user_id = self.request.user)
        queryset_portfoilio_id = models.Portfolio.objects.filter(id=self.kwargs['pk']).values()
        queryset_portfolio = models.Portfolio.objects.all()
        queryset_market = models.Market.objects.all()
        queryset_market_values = models.Market.objects.values()

# determination of each asset in portfolio
        coin = queryset_portfoilio_id[0]['type_id']
        each_asset = []
        for j in queryset_portfolio_user.values():
            if j['type_id'] == coin:
                each_asset.append({'amount':j['amount'],
                                'price_paid':j['price_paid'],
                                'date_created':j['date_created'],
                                'status':j['status']})

        context['each_asset']= each_asset

# determination of each asset in portfolio
        portfolio=[]
        for item in queryset_portfolio_user:
                portfolio.append(({'type':item.type.coin,'amount':item.amount,
                'status':item.status}))
        context ['portfolio'] = portfolio

#  Total Asset of each coin:
        portfolioList = total_assets(queryset_portfolio)
        context['asset']= portfolioList

# Value of each coin in DetailView
        for i in queryset_market_values:
            if coin == i['id']:
                each_coin = i['coin']
        for i in portfolioList:
            if each_coin == i['name']:
                overal = i['asset']
        context['overal'] = overal

        return context


class PortfolioDelete(LoginRequiredMixin,generic.DeleteView):
    model = models.Portfolio
    success_url = reverse_lazy("portfolio:portfolio")





# Function

# Total asset of each coin
def total_assets(queryset_portfolio):

    portfolio=[]
    for item in queryset_portfolio:
            portfolio.append(({'type':item.type.coin,'amount':item.amount,
            'status':item.status}))


    portfolioList = []
    unique = set()
    for i in range(len(portfolio)):
        for j in range(len(data)):
            if portfolio[i]['type'] == data[j]['name']:
                unique.add(portfolio[i]['type'])
    unique = list(unique)
    for i in range(len(unique)):
        asset = 0
        for j in range(len(portfolio)):
            if unique[i] == portfolio[j]['type'] and portfolio[j]['status'] == 'Buy':
                asset += portfolio[j]['amount']
            elif unique[i] == portfolio[j]['type'] and portfolio[j]['status'] == 'Sell':
                asset -= portfolio[j]['amount']
        for x in data:
            if x['name'] == unique[i]:
                current_price = x['current_price']
        if asset > 0 :
            portfolioList.append({'name':unique[i],'asset':asset,
            'current_price':current_price, 'value': asset * current_price})

        elif asset < 0 :
            portfolioList.append({'name':unique[i],'asset': 'The asset can not be negative',
            'current_price':current_price, 'value':0})

    return portfolioList
