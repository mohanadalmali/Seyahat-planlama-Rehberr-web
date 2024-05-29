from django.http import HttpResponse
from django.shortcuts import  render,redirect
from django.contrib import messages
from Seyahat.models import services
from . models import abouts,IndexPage
from . models import ContactMessage
def index(request):
  homepage_services = services.objects.filter(show_on_homepage=True) 
  index_pages=IndexPage.objects.all()
  return render(request,'index.html',{'index_pages':index_pages,'homepage_services': homepage_services,
  })
def about(request):
  abouts_pages=abouts.objects.all()
  return render(request, 'about.html',{'abouts_pages': abouts_pages})
def blog(request):
  return render(request,'blog.html')

def contact(request):
  if request.method == "POST":
    form=ContactMessage()
    name=request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')
    form.name=name
    form.email=email
    form.message=message
    form.save()
   
  return render(request , 'contac.html')
      
  