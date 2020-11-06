


from django.urls import path
from .views import home_view,app_home

urlpatterns = [
    path('',home_view,name="home page"),
    path('home/',app_home, name="app home page")
]