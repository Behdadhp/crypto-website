from market import views
from django.urls import path

app_name = 'market'

urlpatterns = [
    path('', views.MarketListView.as_view(),name='market_list'),
    path('update/<int:pk>',views.MarketUpdateView.as_view(),name='update'),
    path('more',views.MarketListMoreView.as_view(),name='more'),
]
