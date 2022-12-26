from django.views.generic import TemplateView
from django_tables2 import MultiTableMixin

from crypto_website import tables
from market.api import data


class HomePage(TemplateView, MultiTableMixin):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = tables.IndexMarketTable(data[:10])
        context["table"] = table

        return context


class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class AboutPage(TemplateView):
    template_name = 'about.html'
