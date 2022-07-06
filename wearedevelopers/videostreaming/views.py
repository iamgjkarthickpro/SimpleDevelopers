from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import Videos
from django.views.generic import DetailView, ListView,View

#import vimeo

# Create your views here.
# django fucntion based view
def videostreaminghome(request):
    return render(request,'videostreaming/videostreaminghome.html')

# django generic based view
class VideoStreamingHome(ListView):
    model = Videos
    paginate_by = 9
    template_name = 'videostreaming/videostreaminghome.html'

"""
# django rest_framework view
class VideoStreamingHome(APIView):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'videostreaming/videostreaminghome.html'
    def get(self,request):
        return Response()

"""