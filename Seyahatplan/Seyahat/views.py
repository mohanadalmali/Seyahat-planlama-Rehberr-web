
from django.shortcuts import   get_object_or_404, render
from . models import  ServiceDetail, catagori, gezilecekdetai, gezilecekyer, services, servicic

def service(request):
  Service_page = services.objects.all()
  query=request.GET.get('search')
  if query:
    Service_page=Service_page.filter(title__icontains=query)#arama ilgil modelin title göre yapılıyor buda servic modele göre yaptım kucuk buyuk harf önemsiz 
  context={'Service_page':Service_page}
  return render(request,'services.html',context)

def servicdatai(request,id):
  service = get_object_or_404(services, id=id)
  category= get_object_or_404(catagori, id=id)
  Service_page = services.objects.filter(Catagori=category)
  #catagorisi aynı eşit ise bilgi verecek değlse vermez yanı kısaca ilgil servic bilgileri gelecek başlık fotoğraf açıklama
  detai=ServiceDetail.objects.filter(service=service, Catagori=category)
  #servic detai bilgilerini service ve catagori bilgisi eşit olanlar gelecek fitreleme yapılacak 
  servicics = servicic.objects.filter(service_detail__in=detai)
    
  gezilecek_yerler = gezilecekyer.objects.filter(service_detail__in=detai)
  context={
    'gezilecek_yerler':gezilecek_yerler,
    'servicics':servicics,
    'detai':detai,
    'id':id,
    'Service_page':Service_page,
    'service':service,
    'category':category,
  }
  return render(request ,'servicesdetia.html',context)

def search_service(request):
    if request.method=="POST":
      search=request.POST['search']
      arama=services.objects.filter(name__contains=search)
      context={'search':search,'arama':arama}
      return render(request, 'search_services.html',context)
    
    
def rotadetai(request,id):
  service = get_object_or_404(services, id=id)
  category= get_object_or_404(catagori, id=id)
  detai = get_object_or_404(ServiceDetail, id=id)
    # Fetch the specific gezilecekyer object by its ID
  gezilecekye = get_object_or_404(gezilecekyer, id=id)
  gezilecekyerdetai = get_object_or_404(gezilecekdetai, id=id)
  
  
    # Filter gezilecekdetai objects related to the specific gezilecekyer
  gezilecekdet = gezilecekdetai.objects.filter(gezilecekyer__GezilecekYer=gezilecekyerdetai.title)
  context = {
        'gezilecekyerdetai':gezilecekyerdetai,
        'gezilecekdet':gezilecekdet,
        'gezilecekye':gezilecekye,
        'detai': detai,
        'service':service,
        'category':category,
    }
  return render(request,'rotadetai.html',context)