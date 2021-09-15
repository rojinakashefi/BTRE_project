from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtors')
    list_display_links = ('id','title')
    list_editable = ('is_published',)
    list_per_page=(25)
    list_filter = ('price','realtors')
    search_fields = ('title','description','address','city','state','zip','price')

admin.site.register(Listing,ListingAdmin)

# Register your models here.
