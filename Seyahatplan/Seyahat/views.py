from unicodedata import category
from django.shortcuts import   get_object_or_404, render

from . models import  catagori, services
def service(request):
  Service_page = services.objects.all()
  context={'Service_page':Service_page}
  return render(request,'services.html',context)

def servicdatai(request,id):
  category = get_object_or_404(catagori, id=id)

    # Bu kategoriye ait olan services kayıtlarını al
  services_in_category = services.objects.filter(Catagori=category)

  Service_page = services.objects.all()
  context={'id':id,'Service_page':Service_page,'category': category,
        'services_in_category': services_in_category}
  return render(request ,'servicesdetia.html',context)


