from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include("django.contrib.auth.urls", )),
    path('welcome/', views.WelcomePage.as_view(), name='welcome'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('market/', include('market.urls', namespace='market')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('about/', include('about.urls', namespace='about')),
]

# if settings.DEBUG:
#     import debug_toolbar

#     urlpatterns +=[
#         path('__debug__/',include(debug_toolbar.urls))
#     ]
