from django.contrib import admin

# Register your models here.
from .models import clientdetails1

admin.site.site_header='We Plan Solutions'

class clientdetails1Admin(admin.ModelAdmin):
    list_display=('emp_id','client_company_name','client_company_name','client_package_code','client_students_count','amount_to_be_paid')
admin.site.register(clientdetails1,clientdetails1Admin)