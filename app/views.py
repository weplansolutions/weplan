from django.shortcuts import render
from django.contrib.auth.models import auth, User
from .models import clientdetails1

# Create your views here.
def index(request):
    return render(request,'index.html')

def eiplans(request):
    return render(request,'eiplans.html')
def internship(request):
    return render(request,'internships.html')
def workshop(request):
    return render(request,'workshops.html')
def seminar(request):
    return render(request,'seminars.html')
def sciencefair(request):
    return render(request,'sciencefair.html')
def collab(request):
    return render(request,'collaborations.html')
def login(request):
    return render(request,'login.html')
def loginchoose(request):
    return render(request,'loginchoose.html')
def institution(request):
    return render(request,'institutionlogin.html')
def logindata(request):
    
    if request.method=='POST':
        usname=request.POST.get('user')
        psword=request.POST.get('password')

        user=auth.authenticate(username=usname, password=psword)

        if user is not None:
            auth.login(request, user)
            return render(request,'employee.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

def client(request):
    if request.method == 'POST':
           client=clientdetails1()
           client.emp_id=request.POST.get('empid')
           client.emp_mailid=request.POST.get('emp_mailid')
           client.client_company_name=request.POST.get('college')
           client.client_company_type=request.POST.get('type')
           client.client_address=request.POST.get('subject')
           client.client_package_details=request.POST.get('package')
           client.client_package_code=request.POST.get('code')
           client.client_students_count=request.POST.get('count')
           client.academic_year=request.POST.get('year')
           client.amount_to_be_paid=request.POST.get('amount')
           client.save()
           return render(request, 'employee.html')
    else:
        return render(request, 'registration.html')
def registered(request):
    empid=request.POST.get('search')
    obj1=clientdetails1.objects.values().filter(emp_id=empid)
    return render (request,'analysis.html',{'empid':empid,'obj1':obj1})

def about(request):
    return render(request,'about.html')
def ourteam(request):
    return render(request,'ourteam.html')
def careers(request):
    return render(request,'careers.html')
def terms(request):
    return render(request,'terms&conditions.html')
def contact(request):
    return render(request,'contact.html')
def check(request):
    return render(request,'analysis.html')
def registration(request):
    return render(request,'registration.html')