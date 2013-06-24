# Create your views here.
from django.http import HttpResponse
import  datetime

def test(request,value1,value2):
    if value1!="":
        html="第一个参数是"+str(value1)
    if value2!="":
        html+="第二个参数是"+str(value2)
    return HttpResponse(html)

def hello(request):
    now = datetime.datetime.now()
    html = "Hello,time is " + str(now)
    return HttpResponse(html)