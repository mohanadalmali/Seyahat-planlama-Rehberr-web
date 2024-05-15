from django.urls import path
from . import views 
urlpatterns = [
  path('', views.index,name="index"),
  path('about', views.about,name='about'),
  path('blog', views.blog,name='blog'),
  path('contact', views.contact_view,name='contact'),
]