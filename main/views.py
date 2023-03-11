from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout #import authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count
from .models import Settings

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalDeleteView
)
from django.urls import reverse_lazy

from .forms import *
from .models import *

import json

# Create your views here.
def homepage(request):
    return render(request = request, template_name='main/home.html')

def home(request):
    return render(request = request, template_name='main/home.html')

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("/home")

@login_required(redirect_field_name='/home', login_url='/login')
def hotspot_request(request):
    context = {}
    return render(request= request, template_name="main/hotspot.html", context = context)

@login_required(redirect_field_name='/home', login_url='/login')
def rules_request(request):
    context = {}
    return render(request= request, template_name="main/rules.html", context = context)

@login_required(redirect_field_name='/home', login_url='/login')
def forwarders_request(request):
    context = {}
    return render(request= request, template_name="main/forwarders.html", context = context)

# Upload Settings
def upload_setting(req):
    data = json.load(req)
    # result_list = list(Hotspots.objects.filter(key = data.get('key'))\
    #             .values(
    #                     'key',
    #                     'lat',
    #                     'lon',
    #                     'gwid',
    #                     'id'))
    setting = Settings.objects.get(id=1);
    setting.settings = data.get('data');
    setting.save();
    return JsonResponse('success', safe = False)
def download_setting(self):
    ret = list(Settings.objects.filter(id = 1)\
                .values(
                        'settings'))
    return JsonResponse(ret[0], safe = False)
# Get Hotspots
def get_hotspots(self):
    result_list = list(Hotspots.objects.all()\
                .values(
                        'name',
                        'key',
                        'port',
                        'ip',
                        'gpid',
                        'gwid',
                        'rfcid',
                        'lat',
                        'lon',
                        'weight',
                        'txg',
                        'id'))
  
    return JsonResponse(result_list, safe=False)

def verify_duplicate(req) :
    data = json.load(req)
    result_list = list(Hotspots.objects.filter(key = data.get('key'))\
                .values(
                        'key',
                        'lat',
                        'lon',
                        'gwid',
                        'id'))
    return JsonResponse(result_list, safe = False)
# Add Hotspot
class add_hotspot(BSModalCreateView):
    template_name = 'main/modals/add_hotspot.html'
    form_class = HotspotsModelForm
    success_message = 'Success: Hotspot was created.'
    success_url = '/hotspots'
    
# Delete Hotspot
class delete_hotspot(BSModalDeleteView):
    model = Hotspots
    template_name = 'main/modals/delete_hotspot.html'
    success_message = 'Success: Hotspot was deleted.'
    success_url = '/hotspots'

# Update Hotspot
class update_hotspot(BSModalUpdateView):
    model = Hotspots
    template_name = 'main/modals/update_hotspot.html'
    form_class = HotspotsModelForm
    success_message = 'Success: Hotspot was updated.'
    success_url = '/hotspots'
    
# Get Rules
def get_rules(self):
    result_list = list(Hotspots.objects.all()\
                .values(
                        'name',
                        'key',
                        'port',
                        'ip',
                        'gpid',
                        'gwid',
                        'txg',
                        'id'))
  
    return JsonResponse(result_list, safe=False)

def get_groups(self):
    result_list = list(Hotspots.objects\
        .values('gpid')
        .annotate(dcount=Count('gpid'))
        .order_by('gpid'))
    return JsonResponse(result_list, safe = False)

def make_rule(req):
    data = json.load(req)
    result_list = list(Hotspots.objects.filter(gpid = data.get('gpid'))\
                .values(
                        'key',
                        'lat',
                        'lon',
                        'gwid',
                        'weight',
                        'txg',
                        'id'))
    return JsonResponse(result_list, safe = False)

def make_rules(self):
    result_list = list(Hotspots.objects.all()\
                .values(
                        'key',
                        'lat',
                        'lon',
                        'gpid',
                        'gwid',
                        'weight',
                        'txg',
                        'id'))
  
    return JsonResponse(result_list, safe=False)

def make_fwrd_rule(self):
    result_list = {}
    result_list['fwrd'] = list(Forwarders.objects.all()\
                .values(
                        'gpid',
                        'gwid',
                        'id'))
    
    result_list['hotspot'] = list(Hotspots.objects.all()\
                .values(
                        'gpid',
                        'gwid',
                        'id'))
  
    return JsonResponse(result_list, safe=False)
      
# Get Forwarders
def get_forwarders(self):
    result_list = list(Forwarders.objects.all()\
                .values(
                        'name',
                        'gwid',
                        'port',
                        'ip',
                        'id',
                        'gpid'))
  
    return JsonResponse(result_list, safe=False)

# Add Forwarder
class add_forwarder(BSModalCreateView):
    template_name = 'main/modals/add_forwarder.html'
    form_class = ForwardersModelForm
    success_message = 'Success: Forwarder was created.'
    success_url = '/forwarders'
    
# Delete Forwarder
class delete_forwarder(BSModalDeleteView):
    model = Forwarders
    template_name = 'main/modals/delete_forwarder.html'
    success_message = 'Success: Forwarder was deleted.'
    success_url = '/forwarders'

# Update Forwarder
class update_forwarder(BSModalUpdateView):
    model = Forwarders
    template_name = 'main/modals/update_forwarder.html'
    form_class = ForwardersModelForm
    success_message = 'Success: Forwarder was updated.'
    success_url = '/forwarders'