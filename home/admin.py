from django.contrib import admin
from .models import CompanyDetails

@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    """
    The admin definition for the CompanyDetails CMS
    """
    list_display = ('email', 'phone_number', 'street_address1', 'street_address2', 'town_or_city', 'postcode',)