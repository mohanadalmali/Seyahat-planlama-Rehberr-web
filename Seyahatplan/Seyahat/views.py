from unicodedata import category
from django.shortcuts import   get_object_or_404, render

from . models import  ServiceDetail, catagori, services
def service(request):
  Service_page = services.objects.all()
  context={'Service_page':Service_page}
  return render(request,'services.html',context)

def servicdatai(request,id):
  category = get_object_or_404(catagori, id=id)
  service = get_object_or_404(services, id=id)
    
  details = service.details.all()
  services_in_category = services.objects.filter(Catagori=category)
  detail1ve2=ServiceDetail.objects.filter(Catagori=category,service=service)

  Service_page = services.objects.all()
 
  context={'id':id,'category': category,'Service_page':Service_page,'services_in_category': services_in_category,'detail1ve2':detail1ve2,'service': service,
        'details': details,}
  return render(request ,'servicesdetia.html',context)

