from django.contrib import admin
from .models import PhoneCheck

class PhoneCheckAdmin(admin.ModelAdmin):
    list_display = (
        'phone',
        'code',
        'cleared', 
    )
    list_filter = ( 'phone',)

admin.site.register(PhoneCheck, PhoneCheckAdmin)    