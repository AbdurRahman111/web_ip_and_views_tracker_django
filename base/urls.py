from django.urls import  path
from . import views

urlpatterns = [
    path('',views.fun),
    path('about',views.about),
    #path('track/<slug:slug>', views.track_page,name="home.html")
    
]