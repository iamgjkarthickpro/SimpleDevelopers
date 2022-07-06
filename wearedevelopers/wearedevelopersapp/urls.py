from django.urls import path
from .import views
from .views import ContactUs,Home,AboutUs,Blog,Trial,SearchResult,BlogDetails,TrialDetails
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home), # funcion based url
    #path('', TemplateView.as_view(template_name="wearedevelopersapp/home.html")), # django class based url
    #path('', Home.as_view()), # django rest framework based url
    #path('contactus/',views.contactus), # funcion based url
    #path('contactus/',Contactus.as_view()), # django class based url
    path('contactus/',ContactUs.as_view()), # django rest framework based url
    #path('aboutus/',views.aboutus), # funcion based url
    #path('aboutus/', TemplateView.as_view(template_name="wearedevelopersapp/aboutus.html")), # django class based url
    path('aboutus/', AboutUs.as_view()), # django rest framework based url
    #path('blogs/',views.blog), # funcion based url
    path('blogs/', Blog.as_view()), # django generic class based url
    #path('blogs/', Blog.as_view()), # django rest framework based url
    #path('trials/',views.trial), # funcion based url
    path('trials/', Trial.as_view()), # django generic class based url
    #path('trials/', Trial.as_view()), # django rest framework based url
    #path('searchresult/',views.searchresult), # funcion based url
    path('searchresult/', SearchResult.as_view()), # django generic class based url
    #path('searchresult/', SearchResult.as_view()), # django rest framework based url
    #path('blogdetails/<int:id>/',views.blogdetails), # funcion based url
    path('blogdetails/<int:pk>/', BlogDetails.as_view()), # django generic class based url
    #path('blogdetails/<int:id>/', BlogDetails.as_view()), # django rest framework based url
    path('signup/',views.signup), # funcion based url
    #path('trialsdetails/<int:pk>/', TrialDetails.as_view()), # django generic class based url
    #path('trialsdetails/<int:pk>/', TrialDetails.as_view()), # django rest framework based url
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),  
    path('validate_username/',views.validate_username),
    path('validate_email/',views.validate_email),
    path('otp/',views.otp),  
    path('signin/',views.signin,name='signin'),
    path('logout/',views.signout),
    path('addblog/', views.addblog), # django generic class based url
    path('editblog/<int:id>/', views.editblog), # django generic class based url
    path('deleteblog/<int:id>/', views.deleteblog), # django generic class based url
    
]   