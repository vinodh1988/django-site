from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
# get datetime 
import datetime 
  
# create a function 
def home_view(request): 
    # fetch date and time 
    now = datetime.datetime.now() 
    # convert to string 
    html = "Time is {}".format(now) 
    # return response 
    return HttpResponse(html) 

def app_home(request):
    return render(request,'apphome.html', context={'name':'Applicants App'})
