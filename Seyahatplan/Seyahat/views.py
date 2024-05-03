from django.shortcuts import   render

from . models import  services
def service(request):
  Service_page = services.objects.all()
  context={'Service_page':Service_page}
  return render(request,'services.html',context)

def servicdatai(request,id):
  return render(request ,'servicesdetia.html',{'id':id})


