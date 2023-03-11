from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage, name="packet_manager"),
    path("home", views.home, name="packet_manager"),
    path("login", views.login_request, name='login'),
    path("logout", views.logout_request, name= "logout"),
    path("hotspots", views.hotspot_request, name="hotspots"),
    path("rules", views.rules_request, name="rules"),
    path("forwarders", views.forwarders_request, name="forwarders"),
    
    # Hotspot url
    path('hotspots/get_hotspots', views.get_hotspots, name='get_hotspots'),
    path('hotspots/add_hotspot', views.add_hotspot.as_view(), name='create_hotspots'),
    path('hotspots/update_hotspot/<int:pk>', views.update_hotspot.as_view(), name='update_hotspot'),
    path('hotspots/delete_hotspot/<int:pk>', views.delete_hotspot.as_view(), name='delete_hotspot'),
    path('hotspots/verify_duplicate', views.verify_duplicate, name='verify_duplicate_gateway'),
    path('hotspots/get_groups', views.get_groups, name='get_group_ids'),
    path('hotspots/upload_setting', views.upload_setting, name='upload_setting'),
    path('hotspots/download_setting', views.download_setting, name='download_setting'),
    
    # Rule url
    path('rules/get_rules', views.get_rules, name='get_rules'),
    path('rules/make_rule', views.make_rule, name='make_rule'),    
    path('rules/make_rules', views.make_rules, name='make_rules'),    
    path('forwarders/make_fwrd_rule', views.make_fwrd_rule, name='make_fwrd_rule'),    
    
    # Forwarder url
    path('forwarders/get_forwarders', views.get_forwarders, name='get_forwarders'),
    path('forwarders/add_forwarder', views.add_forwarder.as_view(), name='create_forwarders'),
    path('forwarders/update_forwarder/<int:pk>', views.update_forwarder.as_view(), name='update_forwarder'),
    path('forwarders/delete_forwarder/<int:pk>', views.delete_forwarder.as_view(), name='delete_forwarder'),
    
    # Settings url
]
