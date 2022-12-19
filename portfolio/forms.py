from django import forms
from .models import Portfolio


class CreatePortfolio(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('date', 'amount', 'type', 'price_paid', 'status')
