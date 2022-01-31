from django import forms
from .models import Portfolio
from market.models import Market


class CreatePortfolio(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ('date','amount','type','price_paid','status')
