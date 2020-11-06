from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
# get datetime 
import datetime 

from .models import Applicants
  
# create a function 
def home_view(request): 
    # fetch date and time 
    now = datetime.datetime.now() 
    # convert to string 
    html = "Time is {}".format(now) 
    # return response 
    return HttpResponse(html) 

def app_home(request):
    applicants = Applicants.objects.all()
    print(applicants)
    context = {
        'applicants': applicants,
        'name':'Applicatns App'
    }
    
    return render(request,'apphome.html', context)
