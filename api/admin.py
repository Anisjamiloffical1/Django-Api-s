from django.contrib import admin
from api.models import Company, Employee
# Register your models here.
#customize  the admin interface
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'loaction', 'type', 'about')
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'position', 'company')
    list_filter = ('company',)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
