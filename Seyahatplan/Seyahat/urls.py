from django.urls import path
from . import views
urlpatterns = [
  path('', views.service,name='services'),
  path('<int:id>', views.servicdatai,name='servicdatai'),
  path('search/', views.search_service, name='search_service'),
  
] 