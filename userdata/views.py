from .models import 
from django.http import HttpResponse
import json

# Create your views here.
def user_task(request):
    req = json.load(request)
    t = 