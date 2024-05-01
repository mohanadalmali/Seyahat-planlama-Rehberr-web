from django.http import HttpResponse
from django.shortcuts import render

from websi.models import IndexPage, abouts

# Create your views here.
def index(request):
  index_pages = IndexPage.objects.all()
  return render(request,'index.html',{'index_pages': index_pages})
def about(request):
  abouts_pages=abouts.objects.all()
  return render(request, 'about.html',{'abouts_pages': abouts_pages})
def blog(request):
  return render(request,'blog.html')
def contact(request):
  return render(request,'contact.html')