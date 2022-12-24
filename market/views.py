from django.views.generic import (UpdateView)
from django_tables2 import SingleTableView

from portfolio import models
from .api import data
from . import tables


class MarketListView(SingleTableView):
    context_object_name = 'markets'
    model = models.Market

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = data
        table = tables.MarketTable(data)
        table.paginate(page=self.request.GET.get("page", 1), per_page=15)
        context["table"] = table
        return context


class MarketUpdateView(UpdateView, ):
    fields = ("price",)
    model = models.Market
