from . import models
from django.views.generic import (TemplateView, ListView, UpdateView)
from portfolio import models
from .api import data


class MarketListView(ListView):
    context_object_name = 'markets'
    model = models.Market

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = data

        return context


class MarketListMoreView(TemplateView):
    template_name = 'market/market_list_more.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = models.Portfolio.objects.all()
        context['data'] = data

        return context


class MarketUpdateView(UpdateView, ):
    fields = ("price",)
    model = models.Market
