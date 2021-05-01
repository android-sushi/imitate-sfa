from django.contrib import admin
from .models import Company, Person, Info, Note, Schedule, Product, StockControl, Weather

admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Info)
admin.site.register(Note)
admin.site.register(Schedule)
admin.site.register(Product)
admin.site.register(StockControl)
admin.site.register(Weather)
