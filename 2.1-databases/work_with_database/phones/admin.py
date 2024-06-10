from django.contrib import admin
from .models import Phone

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'lte_exists', 'slug')
    list_display_links = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',), }



