from django.contrib import admin
from .models import MyModel


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name','price','quantity')

admin.site.register(MyModel, MyModelAdmin)
