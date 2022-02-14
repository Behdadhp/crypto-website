from django.urls import path
from about import views

app_name = 'about'

urlpatterns =[
    path('submitted',views.SubmittedPage.as_view(),name='submitted'),
    path('', views.ContactUsCreateView.as_view(),name='contactUs')
]
