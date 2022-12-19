from django.views.generic import TemplateView, ListView
from market.api import data


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = data

        return context


class WelcomePage(TemplateView):
    template_name = 'welcome.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class AboutPage(TemplateView):
    template_name = 'about.html'
