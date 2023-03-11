from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import *

class HotspotsModelForm(BSModalModelForm):
    class Meta:
        model = Hotspots
        fields = ['name','key','port','ip','gpid','gwid','rfcid','lat','lon','weight', 'txg']
        
class RulesModelForm(BSModalModelForm):
    class Meta:
        model = Rules
        fields = ['name','gateway_id','port','ip']
        
class ForwardersModelForm(BSModalModelForm):
    class Meta:
        model = Forwarders
        fields = ['name','gwid','port','ip', 'gpid']