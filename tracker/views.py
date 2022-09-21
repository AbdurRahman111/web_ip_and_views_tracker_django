from urllib.parse import uses_relative
from django.http import JsonResponse
from django.shortcuts import render
import httpagentparser
import urllib.request
import json
from device_detector import DeviceDetector
from django.utils.translation import get_language
from datetime import datetime
import re

def about(request):
    tracker(request)
    return render(request,'about.html')


def fun(request):
    tracker(request)
    return render(request,'home.html')
    # Basic user information
    # userInfo = httpagentparser.detect(request.headers.get('User-Agent'))
    # print('User Agent string',userInfo)

    #IP address
    # api = "https://www.iplocate.io/api/lookup/"

    # current_user = request.user
    # if current_user.id is None:
    #     print ('User id',"New user")

    # print('User Information')

    # print('URL',request.get_full_path())
    # time = datetime.now().replace(microsecond=0)
    # print('Time',time)
    # try:
    #     resp = urllib.request.urlopen(api)
    #     result = resp.read()
    #     result = json.loads(result.decode("utf-8"))
    #     print(result)                                                                                                     
    #     userCountry = result["country"]
    #     userContinent = result["continent"]
    #     userCity = result["city"]
    #     userTimeStamp = result['time_zone']
    #     userLatitude = result['latitude']
    #     userLongitude = result['longitude']
    #     userIp = result['ip']
    #     userLocZip = result['postal_code']


    #     print('Country : ',userCountry)
    #     print('Region: ',userContinent)
    #     print('City: ',userCity)
    #     print('Latitude: ',userLatitude)
    #     print('Longitude: ',userLongitude)
    #     print('Timestamp: ',userTimeStamp)
    #     print('Zip code: ',userLocZip)
        
    # except:
    #     print("Could not find: ")

    # ua = request.META['HTTP_USER_AGENT']

    # device = DeviceDetector(ua).parse()
    # print('Device operating system ',device.os_name())
    # print('Device type',device.device_type())
    # print('Device browser',device.client_name() )
    # print('Device brand', device.device_brand())
    # print('Device model',device.device_model())

    # lang = get_language()
    # print('Device language',lang)
    # print(request.user_agent.device)

    return JsonResponse("Hello",safe=False)

def tracker(request):
    #User information

    # IP address
    api = "https://www.iplocate.io/api/lookup/"

    #Basic information
    try:
        resp = urllib.request.urlopen(api)
        result = resp.read()
        result = json.loads(result.decode("utf-8"))
        print(result)                                                                                                     
        userCountry = result["country"]
        userContinent = result["continent"]
        userCity = result["city"]
        userTimeStamp = result['time_zone']
        userLatitude = result['latitude']
        userLongitude = result['longitude']
        userIp = result['ip']
        userLocZip = result['postal_code']

        print('IP address : ',userIp)
        print('Country : ',userCountry)
        print('Region: ',userContinent)
        print('City: ',userCity)
        print('Latitude: ',userLatitude)
        print('Longitude: ',userLongitude)
        print('Timestamp: ',userTimeStamp)
        print('Zip code: ',userLocZip)
        
    except:
        print("Could not find: ")

    # User agent string
    ua = request.META['HTTP_USER_AGENT']
    print('UA',ua)

    #URL of the website
    url = request.get_full_path()
    print('URL',url)

    #Time
    time = datetime.now().replace(microsecond=0)
    print('Time',time)

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
    print('ref',request.META.get('HTTP_REFERER'))
    
    print('Device operating system ',deviceOS)
    print('Device type',deviceType)
    print('Device browser',deviceBrowser)
    print('Device brand', deviceBrand)
    print('Device model',deviceModel)
    print('Device language',deviceLang)
    
# def get_referer_view(request, default=None):
#     ''' 
#     Return the referer view of the current request

#     Example:

#         def some_view(request):
#             ...
#             referer_view = get_referer_view(request)
#             return HttpResponseRedirect(referer_view, '/accounts/login/')
#     '''

#     # if the user typed the url directly in the browser's address bar
#     referer = request.META.get('HTTP_REFERER')
#     if not referer:
#         return default

#     # remove the protocol and split the url at the slashes
#     referer = re.sub('^https?:\/\/', '', referer).split('/')
#     if referer[0] != request.META.get('SERVER_NAME'):
#         return default

#     # add the slash at the relative path's view and finished
#     referer = u'/' + u'/'.join(referer[1:])
#     return referer





    