from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
# get datetime 
import datetime 

from .models import Applicants
from .forms import ApplicantForm
  
# create a function 
def home_view(request): 
    # fetch date and time 
    now = datetime.datetime.now() 
    # convert to string 
    html = "Time is {}".format(now) 
    # return response 
    return HttpResponse(html) 

def app_home(request):
    applicants = Applicants.objects.all()  #returns QuerySet
    print(applicants)
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
    form = ApplicantForm()
    context = {
        'applicants': applicants,
        'name':'Applicatns App',
        'form': form
    }
    
    return render(request,'apphome.html', context)
