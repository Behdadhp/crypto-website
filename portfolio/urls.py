from django.urls import path
from portfolio.views import views
from django.contrib.auth.decorators import login_required

app_name='portfolio'

urlpatterns = [
    path('',login_required(views.PortfolioList.as_view()),name='portfolio'),
    path('new/',views.PortfolioCreate.as_view(), name='create'),
    path('<int:pk>',views.PortfolioDetail.as_view(), name='detail'),
    path('delete/<int:pk>',views.PortfolioDelete.as_view(), name='delete'),
    ]
