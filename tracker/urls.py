from django.http import JsonResponse
import httpagentparser
from django.contrib import admin
from . import views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
]


