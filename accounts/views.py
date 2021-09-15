from contacts.models import Contact
from django.http.response import HttpResponse
from listings import models
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'email is duplicate')
                    return redirect('register')
                else:
                   user = User.objects.create_user(username=username,password=password,first_name=first_name,
                   last_name=last_name,email=email)
                   user.save()
                   messages.success(request,'registered,you can login')
                   return redirect('login')
                #    auth.login(request,user)
                #    messages.success(request,'successfully created a user')
                #    return redirect('index')
                    #looks good 
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else :
        print('FIRST HERE')
        return render(request,'accounts/register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'logged in successfuly')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid informantion')
            return redirect('login')
        # if User.objects.filter(username=username).exists():
        #     if User.objects.filter(password=password).__eq__:
        #         messages.success(request,'loged in successfuly')
        #         return redirect('index')
        #     else:
        #         messages.error(request,'password incorrect')
        #         return redirect('login')
        # else:
        #     messages.error(request,'username doesnt existscreate one')
        #     return redirect('register')
    
    else :
        return render(request,'accounts/login.html')
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {'contacts': user_contacts }
    return render(request,'accounts/dashboard.html',context)
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'successfuly logged out')
    else:
        messages.error(request,'Not logged in to log out')
    return redirect('index')


