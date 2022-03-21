from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth, Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from homepage.models import student
from . templates import decorators
import datetime

# Create your views here.
def home(requests):
    return render(requests,'homepage.html')


def login(requests):
    if requests.method=='POST':
        username=requests.POST['username']
        password=requests.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(requests,user)
            messages.success(requests ,'welcome'+username)
            return redirect('/')
        else:
            messages.info(requests, 'username or password is incorrect')
            return render (requests, 'login.html')
    else:
        return render (requests, 'login.html')

def logout(requests):
    auth.logout(requests)
    return redirect('/')

@decorators.unauthenticated_user
def register(requests):
    if requests.method == 'POST':
        username=requests.POST['username']
        first_name=requests.POST['first name']
        last_name=requests.POST['last name']
        email=requests.POST['email']
        password1=requests.POST['password1']
        password2=requests.POST['password2']

        if password1 != password2:
            return render(requests,'register.html',{'print':'password mismatch'})
        else:
            if (User.objects.filter(email=email).exists()==False) & (User.objects.filter(username=username).exists()==False):
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                print('crated')
                #group=Group.objects.get(name='student')
                #user.groups.add(group)
                student.objects.create(user=user,name=first_name,matric=last_name)
                messages.success(requests ,'succesfully created an account')
                return redirect('/login',)
            else:
                return render(requests,'register.html', {'print':'username or email already exists'})


    else:
        return render(requests,'register.html')

#@decorators.allowed_user(allowed_roles=[''])
@login_required(login_url='/login')
def register2(requests):
    form = UserCreationForm()
    context = {'form':form}
    if requests.method=='POST':
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            form.save()
    return render(requests, 'register2.html',context) 

def courses(requests):

    if requests.method=='POST':
        if requests.POST['options']=='1':
            
            #print(grades)
            return render(requests,'course_addition.html',{'yearss':reversed(range(2011, (datetime.datetime.now().year+1)))})
        elif requests.POST['options']=='3':
            courses=requests.user.student.course_set.all()
            return render(requests,'cgpa.html')

        elif requests.POST['options']=='2':
            return render(requests,'gp.html',{'yearss':reversed(range(2011, (datetime.datetime.now().year+1)))})

        else:
            return render(requests,'homepage.html')
    else:
        courses=requests.user.student.course_set.all()
        #print(grades)
        return render(requests,'courses.html',{'courses':courses})


@login_required(login_url='/login')
def course_addition(requests):
    if requests.method == 'POST':
        name=requests.POST['course name']
        grade=requests.POST['course grade']
        semsester=requests.POST['semester']
        unit=requests.POST['course unit']
        year=requests.POST['year']
    
        requests.user.student.course_set.create(name=name, grade=grade, semsester=semsester, unit=unit, year=year)
        messages.success(requests ,'succesfully added a course')
        return render(requests,'course_addition.html',{'yearss':reversed(range(2011, (datetime.datetime.now().year+1)))})
    else:
        return render(requests,'course_addition.html',{'yearss':reversed(range(2011, (datetime.datetime.now().year+1)))})

@login_required(login_url='/login')
def cgpa(requests):
    r=requests.user.student.course_set.all()
    units=[]
    unit_grade=[]
    for x in r:
        if x.grade=='A':
            units.append(int(x.unit))
            unit_grade.append(int(x.unit)*5)
        if x.grade=='B':
            units.append(int(x.unit))
            unit_grade.append(int(x.unit)*4)
        if x.grade=='C':
            units.append(int(x.unit))
            unit_grade.append(int(x.unit)*3)
        if x.grade=='D':
            units.append(int(x.unit))
            unit_grade.append(int(x.unit)*2)
        if x.grade=='E':
            units.append(int(x.unit))
            unit_grade.append(int(x.unit)*1)
        if x.grade=='F':
            units.append(int(x.unit))
            unit_grade.append(int(x.unit)*0)
    total_units=sum(units)
    total_sums=sum(unit_grade)
    try:
        gpa=total_sums/total_units
        return HttpResponse(gpa)
    except:
        return HttpResponse('you dont have a cgpa yet...please enter courses')

def gp_page(requests):
    if requests.method=='POST':
        year=requests.POST['year']
        semester=requests.POST['semester']
        r=requests.user.student.course_set.all().filter(year=year).filter(semsester=semester)
        print(year)
        print(semester)
        print('mxm dwx exmkx medmqk cjfrjxnekn kneqezwkmxn wemkskewnk')
        print(r)
        units=[]
        unit_grade=[]
        for x in r:
            if x.grade=='A':
                units.append(int(x.unit))
                unit_grade.append(int(x.unit)*5)
            if x.grade=='B':
                units.append(int(x.unit))
                unit_grade.append(int(x.unit)*4)
            if x.grade=='C':
                units.append(int(x.unit))
                unit_grade.append(int(x.unit)*3)
            if x.grade=='D':
                units.append(int(x.unit))
                unit_grade.append(int(x.unit)*2)
            if x.grade=='E':
                units.append(int(x.unit))
                unit_grade.append(int(x.unit)*1)
            if x.grade=='F':
                units.append(int(x.unit))
                unit_grade.append(int(x.unit)*0)
        total_units=sum(units)
        total_sums=sum(unit_grade)

        try:
            gpa=total_sums/total_units
            return render(requests,'final_gp.html', {'courses':r,'gp':gpa,'year':year,'semester':semester})
        except:
            return HttpResponse('you dont have a gp yet, please enter courses')


    else:
        return render('gp.html')


    