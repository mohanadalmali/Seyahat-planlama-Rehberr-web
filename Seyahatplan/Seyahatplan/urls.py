
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('websi.urls')),
  path('Sayahat/', include('Seyahat.urls')),
] + static(settings.MEDİA_URL , document_root=settings.MEDİA_ROOT)