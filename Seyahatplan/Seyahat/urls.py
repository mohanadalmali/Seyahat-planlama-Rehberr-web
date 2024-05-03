from django.urls import path
from . import views
urlpatterns = [
  path('', views.service,name='services'),
  path('<int:id>', views.servicdatai,name='servicdatai'),
  # path('servicesdatai', views.servicdatai,name='servicdatai'),
  
] 