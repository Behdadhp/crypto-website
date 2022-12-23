from django.db.models import Sum, Case, When
from django.views import generic
from django_tables2 import SingleTableView, MultiTableMixin

from portfolio import models
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolio.forms import CreatePortfolio
from django.urls import reverse_lazy

from portfolio import tables
from portfolio.views import calculation as calc


class PortfolioList(LoginRequiredMixin, SingleTableView):
    table_class = tables.ActivityTable
    table_pagination = {"per_page": 5}

    def get_queryset(self):
        return models.Portfolio.objects.all().filter(user_id=self.get_user()).order_by('-date_created')

    def get_user(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.get_user()

        instance_portfolio = calc.Portfolio(models.Portfolio, user)
        asset = instance_portfolio.run()

        context['asset'] = asset
        return context


class PortfolioCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Portfolio
    form_class = CreatePortfolio

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PortfolioDetail(LoginRequiredMixin, generic.DetailView, MultiTableMixin):
    template_name = 'portfolio/portfolio_detail.html'
    table_class = tables.DetailTable

    def get_queryset(self):
        return models.Market.objects.all().filter(id=self.get_coin_id())

    def get_user(self):
        return self.request.user

    def get_coin_id(self):
        return self.kwargs['pk']

    def create_data_query(self):
        return models.Portfolio.objects.filter(user=self.get_user(), type=self.get_coin_id())

    def overall_of_each_asset(self):
        overall = self.create_data_query().annotate(
            total=Case(
                When(status="Buy", then=Sum("amount")),
                When(status="Sell", then=-Sum("amount"))
            ))
        return overall.aggregate(totals=Sum("total"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["overall"] = round(self.overall_of_each_asset()["totals"], 5)
        context["table"] = tables.DetailTable(self.create_data_query())
        return context


class PortfolioDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Portfolio
    success_url = reverse_lazy("portfolio:portfolio")
