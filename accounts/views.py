from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
def register (request):
    if request.method=='GET':
        return render(request, 'register.html')
    elif request.method=='POST':
        first_name=request.POST['first_name'] 
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.info(request,'username is used') 
            return redirect ('register')
             
        else:
            if is_email(email):
                if User.objects.filter(email=email).exists():
                    messages.info(request,'mail is used') 
                    return redirect ('register')
                else:
                    user = User.objects.create_user(username=username,password=password, email=email,first_name=first_name,last_name=last_name)
                    messages.info(request,'user has been created') 
                    user.save()
                    return redirect ('login')    
            else: 
                messages.info(request,'wrong email format') 
                return redirect ('register')
           
            
             

      

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def is_email(value):
    try:
        EmailValidator()(value)
    except ValidationError:
        return False
    else:
        return True

def logout (request):
    auth.logout(request)
    return redirect("/")