from django.views import generic
from django_tables2 import SingleTableView

from portfolio import models
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolio.forms import CreatePortfolio
from django.urls import reverse_lazy

from portfolio.tables import ActivityTable
from portfolio.views import calculation as calc


class PortfolioList(LoginRequiredMixin, SingleTableView):
    table_class = ActivityTable
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


class PortfolioDetail(generic.DetailView, LoginRequiredMixin):
    context_object_name = 'portfolio_details'
    model = models.Portfolio
    template_name = 'portfolio/portfolio_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        pk = self.kwargs['pk']
        instance_asset = calc.Asset(models.Portfolio, user, pk)
        context['each_asset'] = instance_asset.each_asset()
        context['overall'] = instance_asset.overall()
        return context


class PortfolioDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Portfolio
    success_url = reverse_lazy("portfolio:portfolio")
