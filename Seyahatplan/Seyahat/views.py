
from urllib import request
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import   get_object_or_404, render
from . models import  ServiceDetail, catagori,gezilecekyer, services, servicic,gezilecekyerdetai,Comment
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from .forms import Commentform



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
  service_detail = get_object_or_404(ServiceDetail, id=id)
  #catagorisi aynı eşit ise bilgi verecek değlse vermez yanı kısaca ilgil servic bilgileri gelecek başlık fotoğraf açıklama
  detai=ServiceDetail.objects.filter(service=service, Catagori=category)
  #servic detai bilgilerini service ve catagori bilgisi eşit olanlar gelecek fitreleme yapılacak 
  servicics = servicic.objects.filter(service_detail__in=detai)
  gezilecek_yerler = gezilecekyer.objects.filter(service_detail__in=detai)
  comments = Comment.objects.filter(service_detail=service_detail)
  context={
    'comments':comments,
    'service_detail':service_detail,
    'gezilecek_yerler':gezilecek_yerler,
    'servicics':servicics,
    'detai':detai,
    'id':id,
    'Service_page':Service_page,
    'service':service,
    'category':category,
  }
  return render(request ,'servicesdetia.html',context)


def gezilecekyerdetai_view(request, id):
    gezilecekyer_instance = get_object_or_404(gezilecekyer, id=id)
    gezilecekyerdetai_list = gezilecekyerdetai.objects.filter(gezilecekyer=gezilecekyer_instance)
    context = {
        'gezilecekyer': gezilecekyer_instance,
        'gezilecekyerdetai_list': gezilecekyerdetai_list,
    }
    return render(request, 'rotadetai.html', context)

def search_service(request):
    if request.method=="POST":
      search=request.POST['search']
      arama=services.objects.filter(name__contains=search)
      context={'search':search,'arama':arama}
      return render(request, 'search_services.html',context)
    
class addcommentview(CreateView):
        model=Comment
        form_class=Commentform
        template_name='add_comment.html'
        def form_valid(self, form):
            form.instance.service_detail_id = self.kwargs['id']
            return super().form_valid(form)

        success_url = reverse_lazy('servicdatai')
        
        def get_success_url(self):
          return reverse_lazy('servicdatai', kwargs={'id': self.object.service_detail.id})