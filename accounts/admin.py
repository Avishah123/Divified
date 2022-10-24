from django.contrib import admin
from .models import *
# Register your models here.
from import_export.admin import ImportExportModelAdmin

class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

class ListingAdmin(admin.ModelAdmin):
  search_fields = ('Stock_ticker',)
  list_per_page = 125



admin.site.register(nse_bse_stocks, BlogAdmin)  




admin.site.register(User)
admin.site.register(MultipleImage)
admin.site.register(Enduser)
admin.site.register(ticker)

admin.site.register(nse_bse_dividend_alerts, ListingAdmin)
# admin.site.register(nse_bse_dividend_alerts)
