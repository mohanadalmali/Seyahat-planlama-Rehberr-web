from django.contrib import admin
from .models import ContactMessage, IndexPage, abouts

admin.site.register(abouts)
admin.site.register(IndexPage)
admin.site.register(ContactMessage)
