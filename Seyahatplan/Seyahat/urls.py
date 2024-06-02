from django.urls import path
from . import views
from .views import addcommentview
urlpatterns = [
  path('services', views.service,name='services'),
  path('servicdatai/<int:id>', views.servicdatai,name='servicdatai'),
  path('gezilecekyerdetai/<int:id>', views.gezilecekyerdetai_view, name='gezilecekyerdetai'),
  path('search/', views.search_service, name='search_service'),
  path('servicdatai/<int:id>/AddComment', addcommentview.as_view(),name='ADDcomment'),
  
]