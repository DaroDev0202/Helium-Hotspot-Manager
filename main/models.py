from django.db import models

# Create your models here.

# Hotspots
class Hotspots(models.Model):
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=1000)
    port = models.DecimalField(max_digits=5, decimal_places=0)
    ip = models.GenericIPAddressField(protocol="IPv4")
    gpid = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)
    gwid = models.CharField(max_length=250, unique=True)
    lat = models.DecimalField(max_digits=17, decimal_places=13, null=True, blank=True)
    lon = models.DecimalField(max_digits=17, decimal_places=13, null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=0, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True, blank=True)
    txg = models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
# Rules
class Rules(models.Model):
    name = models.CharField(max_length=250)
    gateway_id = models.CharField(max_length=250)
    port = models.DecimalField(max_digits=5, decimal_places=0)
    ip = models.GenericIPAddressField(protocol="IPv4")
    def __str__(self):
        return self.name
    
# Forwarders
class Forwarders(models.Model):
    name = models.CharField(max_length=250)
    gwid = models.CharField(max_length=250, unique = True)
    port = models.DecimalField(max_digits=5, decimal_places=0)
    ip = models.GenericIPAddressField(protocol="IPv4")
    gpid = models.DecimalField(max_digits=3, decimal_places=0)
    def __str__(self):
        return self.name
    
# Settings
class Settings(models.Model):
    settings = models.TextField()
    def __str__(self):
        return self.name