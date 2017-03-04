from django.contrib import admin
from .models import Hotel



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id','name','wilaya','address','created_at','modified_at')








