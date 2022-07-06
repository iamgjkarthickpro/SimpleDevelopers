from django.shortcuts import render

# Create your views here.

def telehome(request):
    return render(request,'telemedicineconsultation/telehome.html')