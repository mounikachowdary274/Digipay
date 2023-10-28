from django.contrib import admin
from transactions.models import Transaction,Credit_Card
# Register your models here.

class Credit_CardAdmin(admin.ModelAdmin):
    list_display=['name','number','year','card_type']
admin.site.register(Transaction)
admin.site.register(Credit_Card,Credit_CardAdmin)