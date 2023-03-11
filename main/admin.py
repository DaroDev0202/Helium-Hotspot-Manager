from django.contrib import admin
from .models import Hotspots 
from .models import Rules 
from .models import Forwarders 
# Register your models here.
admin.site.register(Hotspots)
admin.site.register(Rules)
admin.site.register(Forwarders)