from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

User = get_user_model()


class Market(models.Model):
    coin = models.CharField(max_length=32)
    label = models.CharField(max_length=8)
    price = models.FloatField(max_length=16)

    def __str__(self):
        return (self.coin)

    def get_absolute_url(self):
        return reverse("market:market_list")
