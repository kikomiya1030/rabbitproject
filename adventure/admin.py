from django.contrib import admin
from .models import PyTest

# Register your models here.

class AdventureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(PyTest, AdventureAdmin)