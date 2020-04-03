from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from main.forms import PhotoForm
from django.contrib.auth.models import User, auth
import datetime
from main.models import Image

from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from django.views.generic.edit import CreateView
from main.models import Image
# Create your views here.


    



def photo(request):   
    
    if request.method == 'POST':       
        
        form=PhotoForm(request.POST, request.FILES)
        form.instance.username=request.user
        if form.is_valid():

            form.save()
            
            return redirect('/')
        else:
            return HttpResponse('something went wrong...')
       
    else:
        form=PhotoForm()
        return render(request,'photo.html',{
            'form': form

        })  
  
def success(request): 
    return HttpResponse('successfully uploaded') 