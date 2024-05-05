
# Register your models here.
from django.contrib import admin
from .models import ServiceDetail, catagori,services
admin.site.register(catagori)
admin.site.register(services)
admin.site.register(ServiceDetail)



