from django.contrib import admin
from .models import Blogs,Demo,addcountrycode,mobilenumber
# Register your models here.

admin.site.register(Blogs)
admin.site.register(Demo)
admin.site.register(addcountrycode)
admin.site.register(mobilenumber)