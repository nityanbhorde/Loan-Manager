from django.contrib import admin
from .models import Loan


class LoanAdmin(admin.ModelAdmin):
    list_display = ['name', 'money']
admin.site.register(Loan,LoanAdmin )
# Register your models here.


