from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name="home"),
   path('submit',views.submit,name="submit"),
   path('show',views.show,name="show"),
   path('showdata',views.showdata,name="showdata"),
    
]
