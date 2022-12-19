from django.views import generic
from portfolio import models
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolio.forms import CreatePortfolio
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from portfolio.views.calculation import Asset, Portfolio

User = get_user_model()


class PortfolioList(generic.ListView, LoginRequiredMixin):
    context_object_name = 'portfolio_lists'
    queryset = models.Portfolio.objects.all().order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_req = self.request.user

        instance_portfolio = Portfolio(models.Portfolio, user_req)
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

        user_req = self.request.user
        pk_req = self.kwargs['pk']
        instance_asset = Asset(models.Portfolio, user_req, pk_req)
        context['each_asset'] = instance_asset.each_asset()
        context['overall'] = instance_asset.overall()

        return context


class PortfolioDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Portfolio
    success_url = reverse_lazy("portfolio:portfolio")
