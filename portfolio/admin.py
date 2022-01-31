from django.contrib import admin
from portfolio.models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display=( 'user','date', 'amount', 'type','price_paid' ,'status','date_created')
    list_display_links = ( 'user','type')
    ordering=('-date',)



admin.site.register(Portfolio,PortfolioAdmin)
