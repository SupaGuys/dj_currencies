from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("Hello! It's %s o'clock" % datetime.datetime.now())
