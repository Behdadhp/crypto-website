from django.db import models
from django.urls import reverse
from market.models import Market
from datetime import datetime

from django.contrib.auth import get_user_model
from django import template

User = get_user_model()


register = template.Library()

STATUS = (
    ("Buy", "Buy"),
    ("Sell", "Sell")
)


class Portfolio(models.Model):
    date = models.DateField(default=datetime.now, blank=False, null=False)
    amount = models.FloatField(max_length=8, blank=False, null=False)
    type = models.ForeignKey(Market, related_name='markets', blank=False, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='usernames', blank=False, null=False, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=STATUS)
    date_created = models.DateTimeField(default=datetime.now)
    price_paid = models.FloatField(max_length=16, blank=False, null=False)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("portfolio:portfolio")

    # class Meta:
    #     ordering = ["-date_created"]
