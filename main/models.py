from django.db import models

# Create your models here.

# Hotspots
class Hotspots(models.Model):
    name = models.CharField(max_length=250)
    key = models.CharField(max_length=1000)
    port = models.DecimalField(max_digits=5, decimal_places=0)
    ip = models.GenericIPAddressField(protocol="IPv4")
    gpid = models.DecimalField(max_digits=3, decimal_places=0)
    gwid = models.CharField(max_length=250, unique=True)
    rfcid = models.CharField(max_length=250)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lon = models.DecimalField(max_digits=10, decimal_places=6)
    weight = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    txg = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    
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