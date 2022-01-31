from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings


app_name='accounts'

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
    path('signup/', views.SignUp.as_view(),name="signup"),
    path('your_profile/',views.ProfilePage.as_view(),name='your_profile'),
    path('update/<int:pk>', views.UpdateProfilePage.as_view(),name='update'),
]
