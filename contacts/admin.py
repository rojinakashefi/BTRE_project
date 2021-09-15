from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','listing_id','contact_date')
    list_display_links=('id','name')
    list_per_page = (25)
    search_fields = ('listing','name','email')

admin.site.register(Contact,ContactAdmin)
# Register your models here.
