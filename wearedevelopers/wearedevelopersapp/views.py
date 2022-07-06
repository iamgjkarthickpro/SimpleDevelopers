from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.template.loader import render_to_string  
from django.core.mail import EmailMessage
from django.views import View
from .forms import SignupForm
from .models import Blogs,Demo,addcountrycode, mobilenumber
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import HttpResponseRedirect
from rest_framework.pagination import LimitOffsetPagination
from django.views.generic import DetailView, ListView,View
from twilio.rest import Client
import random
from django.contrib import auth
from django.contrib.auth import login,logout
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes, force_text  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.http import HttpResponse, JsonResponse  
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.db.models.query_utils import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def deleteblog(request,id):
    blog=Blogs.objects.get(id=id)
    blog.delete()
    messages.success(request,'blog deleted successfully')
    return redirect('/blogs/')

def editblog(request,id):
    blog=Blogs.objects.get(id=id)
    if request.method=='POST':
        title= request.POST['title']
        context= request.POST['context']
        image=request.FILES['image']
        book=Blogs(title=title,context=context,image=image,id=id)
        book.save()
        messages.success(request,'blog edited successfully')
        return redirect('/blogs/')
    return render(request,'wearedevelopersapp/editblog.html',{'blog':blog})

def addblog(request):
    if request.method=='POST':
        title= request.POST['title']
        context= request.POST['context']
        image=request.FILES['image']
        book=Blogs(title=title,context=context,image=image)
        book.save()
        messages.success(request,'blog added successfully')
        return redirect('/blogs/')
    return render(request,'wearedevelopersapp/addblog.html')

def signout(request):
    auth.logout(request)
    messages.success(request,'logout successfully')
    return redirect('/trials/')    


def signin(request):    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            print('3')
            username=User.objects.get(email=email).username
        except User.DoesNotExist:
            print('4')
            print('user doesnot exist')
            return redirect('/id',messages.error(request,'user doesnot exist'))             
        user=auth.authenticate(username=username,password=password)        
        try:
            print('5')
            if user is not None:
                print('6')
                if user.is_superuser == 0 and user.is_staff == 0 and user.is_active== 1:
                    print('7')
                    auth.login(request,user)
                    messages.success(request,'login successfully')
                    #return redirect('/signin/')
                elif user.is_superuser == 0 and user.is_staff == 1 and user.is_active== 1:
                    print('8')
                    auth.login(request,user)
                    return redirect('/')
                elif user.is_superuser == 1:                    
                    auth.login(request,user)
                    return redirect('/')
            #return redirect('/id',messages.error(request,'Wrong password'))   
        except:            
            print('10')
            return redirect('/id',messages.error(request,'Error Unknown'))       
    
    return render(request, 'wearedevelopersapp/signin.html',)  

def home(request):
    blogs=Blogs.objects.all()
    return render(request,'wearedevelopersapp/home.html',{'blogs':blogs})

# django rest_framework view
class Home(APIView):        
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'wearedevelopersapp/home.html'
    def get(self,request):                
        return Response()

# django function based view    
def contactus(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        company = request.POST['company']
        industry = request.POST['industry']
        servicesbytechnology = request.POST['servicesbytechnology']
        inquiry = request.POST['inquiry']
        existedclient = request.POST['existedclient']
        suggestion = request.POST['suggestion']
        obj = User.objects.filter(is_superuser=1)
        for i in obj:
            mail_subject='Contact Detail'
            print(mail_subject)
            print(i.username)            
            message =render_to_string('wearedevelopersapp/contactdetail.html', {                                              
                'user':i.username,
                'firstname':firstname,
                'lastname':lastname,
                'email':email,                                                        
                'phone':phone,                                                        
                'country':country,                                                        
                'company':company,                                                        
                'industry':industry,                                                        
                'servicesbytechnology':servicesbytechnology,                                                        
                'inquiry':inquiry,                                                        
                'existedclient':existedclient,                                                        
                'suggestion':suggestion,                                                        
            })  
            print(message)
            to_email = i.email        
            print(to_email)
            email = EmailMessage(  
                        mail_subject,message, to=[to_email]  
            )            
            print(email)
            email.send()   
            
            return redirect('/') 
                   

    return render(request,'wearedevelopersapp/contactus.html')    

# django class based view
class Contactus(View):
    def get(self,request,*args,**kwargs):         
        return render(request,'wearedevelopersapp/contactus.html',{})
    def post(self,request,*args,**kwargs):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        company = request.POST['company']
        industry = request.POST['industry']
        servicesbytechnology = request.POST['servicesbytechnology']
        inquiry = request.POST['inquiry']
        existedclient = request.POST['existedclient']
        suggestion = request.POST['suggestion']
        obj = User.objects.filter(is_superuser=1)
        for i in obj:
            mail_subject='Contact Detail'
            print(mail_subject)
            print(i.username)            
            message =render_to_string('wearedevelopersapp/contactdetail.html', {                                              
                'user':i.username,
                'firstname':firstname,
                'lastname':lastname,
                'email':email,                                                        
                'phone':phone,                                                        
                'country':country,                                                        
                'company':company,                                                        
                'industry':industry,                                                        
                'servicesbytechnology':servicesbytechnology,                                                        
                'inquiry':inquiry,                                                        
                'existedclient':existedclient,                                                        
                'suggestion':suggestion,                                                        
            })  
            print(message)
            to_email = i.email        
            print(to_email)
            email = EmailMessage(  
                        mail_subject,message, to=[to_email]  
            )            
            print(email)
            email.send()   
            return redirect('/')

# django rest_framework view
class ContactUs (APIView):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'wearedevelopersapp/contactus.html'
    def get(self,request):
        return Response()
    def post(self,request):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        company = request.POST['company']
        industry = request.POST['industry']
        servicesbytechnology = request.POST['servicesbytechnology']
        inquiry = request.POST['inquiry']
        existedclient = request.POST['existedclient']
        suggestion = request.POST['suggestion']
        obj = User.objects.filter(is_superuser=1)
        for i in obj:
            mail_subject='Contact Detail'
            print(mail_subject)
            print(i.username)            
            message =render_to_string('wearedevelopersapp/contactdetail.html', {                                              
                'user':i.username,
                'firstname':firstname,
                'lastname':lastname,
                'email':email,                                                        
                'phone':phone,                                                        
                'country':country,                                                        
                'company':company,                                                        
                'industry':industry,                                                        
                'servicesbytechnology':servicesbytechnology,                                                        
                'inquiry':inquiry,                                                        
                'existedclient':existedclient,                                                        
                'suggestion':suggestion,                                                        
            })  
            print(message)
            to_email = i.email        
            print(to_email)
            email = EmailMessage(  
                        mail_subject,message, to=[to_email]  
            )            
            print(email)
            email.send() 
            return HttpResponseRedirect(redirect_to='/')




# django function based view
def aboutus(request):
    return render(request,'wearedevelopersapp/aboutus.html')

# django rest_framework view
class AboutUs(APIView):
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'wearedevelopersapp/aboutus.html'
    def get(self,request):                
        return Response()

# django function based view
def blog(request):
    return render(request,'wearedevelopersapp/blogs.html')

# django generic based view
class Blog(ListView):    
    model = Blogs    
    paginate_by = 3
    template_name = 'wearedevelopersapp/blogs.html'    

"""
# django rest_framework view
class Blog(APIView,LimitOffsetPagination):    
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'wearedevelopersapp/blogs.html'
    def get(self,request):                
        return Response()
        
"""

# django function based view
def blogdetails(request,id):
    return render(request,'wearedevelopersapp/blogdetails.html')

# django generic based view
class BlogDetails(DetailView):    
    model = Blogs
    paginate_by = 9
    template_name = 'wearedevelopersapp/blogdetails.html'    
    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetails,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["category"] = "MISC"        
        return context
"""
# django rest_framework view
class BlogDetails(APIView,LimitOffsetPagination):    
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'wearedevelopersapp/blogdetails.html'
    def get(self,request):                
        return Response()
        
"""

# django function based view
def trial(request):
    object_list=Demo.objects.all()
    return render(request,'wearedevelopersapp/trials.html',{'object_list':object_list})

# django generic based view
class Trial(ListView):    
    model = Demo    
    paginate_by = 1
    template_name = 'wearedevelopersapp/trials.html'    

# django rest_framework view
class Trial(APIView):        
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'wearedevelopersapp/trials.html'
    def get(self,request):                
        return Response()
        
# django function based view
def signup(request):
    
    objs=addcountrycode.objects.all() 
    if request.method=='POST':
        form = SignupForm(request.POST)  
        if form.is_valid():
            print('bbbbbbbbbbbbbbbbbb')              
            user = form.save(commit=False)  
            user.is_active = False  
            user.is_staff = False
            #user.is_staff = True
            user.save()     
            print(user)                
            countrycode=request.POST['countrycode']
            print(countrycode,'once again im the country code')
            mobile=request.POST['mobile']
            
            otp_number=random.randint(1000,9999)
            #mobile='9606632985'
            auth_sid="AC01a351708bbb99f23b8f6d2e99833431"
            auth_token="eb0f818e9e9daa3063d9c35302d6d7cb"

            otp_client=Client(auth_sid,auth_token)

            otp_message=otp_client.messages.create(
                body="your otp is"+str(otp_number),
                from_="+15093162636",
                
                to=countrycode+mobile,
                #to="+91"+mobile,
            )
            print('otp is'+str(otp_number))
            book4=mobilenumber(number=mobile,otp=otp_number,id=1,user=user)
            book4.save()                                         
            current_site = get_current_site(request)  
            print(current_site)
            mail_subject = 'Activation link has been sent to your email id' 
            print(mail_subject) 
            message = render_to_string('wearedevelopersapp/acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()              
            return redirect('/otp/',messages.success(request,'Please confirm otp to complete the registration'))            
            #return render(request,'wearedevelopersapp/signup.html',{'object':object,'objs':objs,'mobile':mobile})
            #return redirect('/signup/'+str(id),messages.success(request,'Please confirm your email address to complete the registration'))            
            
        else:
            
            print(form.errors)
            error=form.errors
            return redirect('/signup/'+str(id),messages.error(request,error))

    return render(request,'wearedevelopersapp/signup.html',{'objs':objs})

def otp(request):        
    if request.method=="POST":
        otp=request.POST['otp']
        try:
            otp=mobilenumber.objects.get(otp=otp).otp        
            print('true condition matched')
            return redirect('/',messages.error(request,"Otp verification completed, continue with email verification to complete process"))
        except:
            return redirect('/otp/',messages.error(request,"wrong otp"))
    return render(request,'wearedevelopersapp/otp.html')

# django function based view
def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        messages.success(request,'Thank you for your email confirmation. Now you can login your account.')
        return redirect('/')
    else:  
        return HttpResponse('Activation link is invalid!')  

# django generic based view
class TrialDetails(DetailView):    
    model = Demo
    paginate_by = 1
    template_name = 'wearedevelopersapp/signup.html'    
    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetails,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        context["category"] = "MISC"        
        return context

# django rest_framework view
class TrialDetails(APIView):        
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)
    template_name = 'wearedevelopersapp/signup.html'
    def get(self,request):                
        return Response()    

# django function based view
def searchresult(request):
    if request.method=='POST':
        search = request.POST['search']
        print(search,'this is searched')

# django generic based view
class SearchResult(View):        
    def post(self,request,*args,**kwargs):
        search = request.POST['search']
        print(search,'this is searched')        
        try:
            blogid=Blogs.objects.get(title__icontains=search).id            
            return redirect('/blogdetails/'+str(blogid))
        except:
            messages.error(request,'result not found')

"""
# django rest_framework view
class SearchResult(APIView):        
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer    
    def post(self,request):
        search = request.POST['search']
        print(search,'this is searched')
        
"""

def validate_username(request):
    username=request.GET.get('username',None)
    data={
        'is_taken': User.objects.filter(username=username).exists()
    }
    if data['is_taken']:
        data['error_message']='A user with this username already exists.'
    return JsonResponse(data)

def validate_email(request):
    email=request.GET.get('email',None)
    data={
        'is_taken': User.objects.filter(email=email).exists()
    }
    if data['is_taken']:
        data['error_message']='A user with this email already exists.'
    return JsonResponse(data)