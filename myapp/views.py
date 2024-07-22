from django.shortcuts import render,redirect
from .models import Users,Todo
from django.contrib import messages
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def registration (request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phonenumber=request.POST['phonenumber']
        password=request.POST['password']
        conformpassword=request.POST['conformpassword']
        emailexists=Users.objects.filter(Email=email)
        if emailexists:
            messages.error(request,'EMAIL ALREADY EXISTS!')
        elif password!=conformpassword:
            messages.error(request,'PASSWORD IS NOT SAME AS ABOVE!')
        else:
            Users(Name=name,Email=email,Phonenumber=phonenumber,Password=password).save()
            return redirect('loginpage')
            
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        current_user=Users.objects.filter(Email=email,Password=password)
        if current_user:
            request.session['Email']=email
            return redirect('addlist')
        else:
            messages.error(request,'INVALID EMAIL ID OR PASSWORD!')

    return render(request,'login.html')

def addtodo(request):
    if 'Email' in request.session :
        current_user=request.session['Email']
        user=Users.objects.get(Email=current_user)
        data=user.user.all()

        if request.method=='POST':
            activity=request.POST['activity']
            date=request.POST['date']
            time=request.POST['time']
            priority=request.POST['priority']
            image=request.FILES.get('image')
            owner=Users.objects.get(Name=user.Name)
            Todo(Activity=activity,Date=date,Time=time,Priority=priority,Image=image,owner=owner).save()
            messages.error(request,'LIST ADDED')
            return redirect('read')
    return render(request,'addlist.html',{'user':user,'data':data})

def read(request):
    if 'Email' in request.session :
        current_user=request.session['Email']
        user=Users.objects.get(Email=current_user)
        data=user.user.all()
    return render(request,'read.html',{'data':data,'user':user})

def update(request,id):
    if 'Email' in request.session :
        current_user=request.session['Email']
        user=Users.objects.get(Email=current_user)
        data=Todo.objects.get(id=id)
    if request.method=='POST':
        activity=request.POST['activity']
        date=request.POST['date']
        time=request.POST['time']
        priority=request.POST['priority']
        image=request.FILES.get('image')
        owner=Users.objects.get(Name=user.Name)
        data.Activity=activity
        data.Date=date
        data.Time=time
        data.Priority=priority
        data.Image=image
        data.owner=owner
        data.save()
        return redirect('read')

    return render(request,'update.html',{'data':data,'user':user})

def delete(request,id):
    data=Todo.objects.get(id=id)
    data.delete()
    return redirect('read')

def logout(request):
    if "Email" in request.session:
        del request.session['Email']
    return redirect('loginpage')


def forgot(request):
    if request.method=='POST':
        email=request.POST['email']
        emailexist=Users.objects.filter(Email=email)
        if emailexist:
            request.session['Email']=email
            
            return redirect('password')
        else:
            messages.error(request,'EMIAL NOT EXISTS!')
    return render(request,'forgot.html')

def password(request):
    if 'Email' in request.session:
        current_user=request.session['Email']
        user=Users.objects.get(Email=current_user)
    return render(request,'password.html',{'user':user})
