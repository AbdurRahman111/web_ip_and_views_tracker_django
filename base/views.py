from time import timezone
from urllib import response
from urllib.parse import uses_relative
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import httpagentparser
import urllib.request
import json
from device_detector import DeviceDetector
from django.utils.translation import get_language
from datetime import datetime
import uuid
from .models import userData

def getcookie(request,id):  
    info  = request.COOKIES.get(id) 
    print(info)

def about(request):
    response = render(request, 'about.html')
    
    if request.COOKIES.get('user_id'):
        user_id  = request.COOKIES.get('user_id')
        device_id = request.COOKIES.get('device_id')

    else:
        print('Cookie does not exist')

        user_id = str(uuid.uuid1())
        device_id = str(uuid.uuid1())
        response.set_cookie(key='user_id', value=user_id)
        response.set_cookie(key='device_id', value=device_id)


    tracker(request,user_id,device_id)
    return response

def getcookie(request,id):  
    info  = request.COOKIES.get(id) 
    print(info)

def track_page(request,page_htm='home.html'):
    response = render(request, page_htm) 
    if request.COOKIES.get('user_id'):
        user_id  = request.COOKIES.get('user_id')
        device_id = request.COOKIES.get('device_id')
    else:
        print('Cookie does not exist')
        user_id = str(uuid.uuid1())
        device_id = str(uuid.uuid1())
        response.set_cookie(key='user_id', value=user_id)
        response.set_cookie(key='device_id', value=device_id)
    tracker(request,user_id,device_id)
    return response

def fun(request):
    #Logic to handle cookies
    #if the cookies are present then the value will be passed to tracker
    #else a new cookie will be created and value will be passed

    #uuid will be used to uniquely indentify users and devices
    response = render(request, 'home.html')
    
    if request.COOKIES.get('user_id'):
        user_id  = request.COOKIES.get('user_id')
        device_id = request.COOKIES.get('device_id')

    else:
        print('Cookie does not exist')

        user_id = str(uuid.uuid1())
        device_id = str(uuid.uuid1())
        response.set_cookie(key='user_id', value=user_id,max_age=60*60*24*30)
        response.set_cookie(key='device_id', value=device_id)


    tracker(request,user_id,device_id)
    return response
        

def tracker(request,user_id,device_id):
    #User information

    # IP address
    api = "https://www.iplocate.io/api/lookup/"

    #Basic information
    try:
        resp = urllib.request.urlopen(api)
        result = resp.read()
        result = json.loads(result.decode("utf-8"))
        userIp = result["ip"]                                                                                                     
        userCountry = result["country"]
        userContinent = result["continent"]
        userCity = result["city"]
        userTimeZone = result['time_zone']
        userLatitude = result['latitude']
        userLongitude = result['longitude']
        userIp = result['ip']
        userLocZip = result['postal_code']
        
    except:
        print("Could not find: ")

    # User agent string
    ua = request.META['HTTP_USER_AGENT']

    #URL of the website
    url = request.get_full_path()

    #Time
    timeStamp = datetime.now().replace(microsecond=0)

    #Device information
    device = DeviceDetector(ua).parse()
    deviceOS = device.os_name()
    deviceType = device.device_type()
    deviceBrowser = device.client_name()
    deviceLang = get_language()
    
    deviceBrand = device.device_brand()
    if deviceBrand == '':
        deviceBrand = 'N/A'
    
    deviceModel = device.device_model()
    if deviceModel == '':
        deviceModel = 'N/A'

    # referer_view = get_referer_view(request)
    ref_url = request.META.get('HTTP_REFERER')

    # if a new user visits the website
    # a new record will be created in the database
    # but if the existing user visits the page again it will increment in the pages number
    try:
        temp = userData.objects.get(
        device_os = deviceOS,
        device_browser = deviceBrowser,
        device_type = deviceType,
        device_model = deviceModel,
        site_url = url,
        referrer_url = ref_url,
        user_agent = ua,
        timezone = userTimeZone,
        location_longitude = userLongitude,
        location_latitude = userLatitude,
        location_country = userCountry,
        location_region = userContinent,
        location_city = userCity,
        location_zip = userLocZip,
        user_ip = userIp,
        user_id = user_id,
        device_id = device_id,
        )

        views = temp.views
        views = views + 1
        temp.views = views
        temp.save()
    except:
        userData.objects.create(
            device_os = deviceOS,
            device_browser = deviceBrowser,
            device_type = deviceType,
            device_model = deviceModel,
            site_url = url,
            referrer_url = ref_url,
            user_agent = ua,
            timestamp = timeStamp,
            timezone = userTimeZone,
            location_longitude = userLongitude,
            location_latitude = userLatitude,
            location_country = userCountry,
            location_region = userContinent,
            location_city = userCity,
            location_zip = userLocZip,
            user_ip = userIp,
            user_id = user_id,
            device_id = device_id,
    )


        

    

    

