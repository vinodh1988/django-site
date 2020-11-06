from django.shortcuts import render

  
# create a function 
def home_view(request): 

    return render(request,'home.html', context={'name':'Vinodh'})