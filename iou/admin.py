from django.contrib import admin
from iou.models import Debt
# Register your models here.
class DebtAdmin(admin.ModelAdmin):
    list_display = ('debt', 'debtor', 'creditor',)
    list_filter = ('debtor',)
    search_fields = ['debtor', 'creditor']

admin.site.register(Debt, DebtAdmin)    