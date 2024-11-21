from django.contrib import admin
from .models import Realtor  # Ensure the correct import path

class RealtorAdmin(admin.ModelAdmin):
    # Adjusted to match the actual fields in the Realtor model
    list_display = ('id', 'name', 'email', 'hire_date')  # List fields present in the model
    list_display_links = ('id', 'name')  # The fields to click on for detail view
    search_fields = ('name',)  # Fields to be searchable
    list_per_page = 25  # Number of items to display per page

admin.site.register(Realtor, RealtorAdmin)
