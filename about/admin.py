from django.contrib import admin
from about.models import ContactUs
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display =('user','date','email','comment')
    list_display_links = ('user','email')
    ordering = ('-date',)


admin.site.register(ContactUs, ContactUsAdmin)
