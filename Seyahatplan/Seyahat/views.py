from django.shortcuts import  render

# from Sayahat.models import Service, ServiceDetail

# def indexservic(request):
  
#   context=dict()
#   context["indexpage"] = IndexPage.objects.all()
def services(request):
#   context=dict()
#   context["Servicepage"] = Service.objects.all()
  return render(request,'services.html')
def servicdatai(request):
#   context=dict()
#   context["ServiceDetailpage"] = ServiceDetail.objects.all()
  return render(request,'servicesdetia.html')