from django.db import models

class catagori(models.Model):
    name=models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name
 
class services(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    Catagori=models.ForeignKey(catagori,null=True, on_delete=models.DO_NOTHING)
    description = models.TextField()
    image = models.ImageField(upload_to="media")
    show_on_homepage = models.BooleanField(default=False)
    
    link_title = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True)
    link_title2 = models.CharField(max_length=100, blank=True)
    link_url2 = models.URLField(blank=True)
    
    main_title = models.CharField(max_length=200)
    main_title2 = models.CharField(max_length=200)

    
    def __str__(self):
        return self.title

class ServiceDetail(models.Model):
    service = models.ForeignKey(services, related_name='details', on_delete=models.CASCADE)
    
    Catagori=models.ForeignKey(catagori,null=True, on_delete=models.DO_NOTHING)
    
    title1 = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to="media")
    description1 = models.TextField()
    
    title2 = models.CharField(max_length=200)
    image2 = models.ImageField(upload_to="media")
    description2 = models.TextField()
    
    def save(self, *args, **kwargs):
        # ServiceDetail öğesi oluşturulduğunda, ilgili services ve category öğelerini bulun
        service = self.service

        # ServiceDetail öğesini ilgili servicenin detayına ekleyin
        if not self.pk:  # Eğer öğe henüz kaydedilmemişse
            super().save(*args, **kwargs)  # Öğeyi kaydedin
            service_detail_id = self.pk  # Yeni oluşturulan ServiceDetail öğesinin ID'sini alın
            service_detail = ServiceDetail.objects.get(pk=service_detail_id)  # Oluşturulan ServiceDetail öğesini getirin
            # İlgili servicenin detayına bu ServiceDetail öğesini ekleyin
            service.details.add(service_detail)
            service.save()
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title1
    