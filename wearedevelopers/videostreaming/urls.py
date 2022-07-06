from django.urls import path
from .import views
from .views import VideoStreamingHome
from django.views.generic import TemplateView

urlpatterns = [
    #path('',views.videosteamhome), # funcion based url
    #path('', TemplateView.as_view(template_name="videosteamhome/videosteamhome.html")), # django class based url
    path('', VideoStreamingHome.as_view()), # django rest framework based url    
]   
