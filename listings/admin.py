from django.contrib import admin
from.models import Listings
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    # this helps to add more header into the page
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    # adding the link for id and tile
    list_display_links = ('id', 'title')

    # adding the filter button on site
    list_filter = ('realtor',)

    # making function able of published or unpublished
    list_editable = ('is_published',)

    # adding the searchfield function
    search_fields = ('title', 'description', 'address',
                     'city', 'state', 'zipcode', 'price')

    # adding total amount of listing per page
    list_per_page = 25


admin.site.register(Listings, ListingAdmin)
