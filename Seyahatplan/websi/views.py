from django.http import HttpResponse
from django.shortcuts import redirect, render
from Seyahat.models import services
from . models import abouts,ContactMessage,IndexPage

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

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessage(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success_url') 
    else:
        form = ContactMessage()
    return render(request, 'contact.html', {'form': form})