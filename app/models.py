from django.db import models

# Create your models here.

class clientdetails1(models.Model):
    emp_id= models.CharField(max_length=300)
    emp_mailid= models.CharField(max_length=300)
    client_company_name=models.CharField(max_length=300)
    client_company_type=models.CharField(max_length=300)
    client_address=models.CharField(max_length=3000)
    client_package_details=models.CharField(max_length=300)
    client_package_code=models.CharField(max_length=300)
    client_students_count=models.CharField(max_length=300)
    academic_year=models.CharField(max_length=300)
    amount_to_be_paid=models.CharField(max_length=300)
