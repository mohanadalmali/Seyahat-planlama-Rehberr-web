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
    
    def __str__(self):
        return self.title


class ServiceDetail(models.Model):
    service = models.ForeignKey(services, related_name='details', on_delete=models.CASCADE)    
    Catagori=models.ForeignKey(catagori,null=True, on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=50, null=True,default="")
    
    
    link_title = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True)
    link_title2 = models.CharField(max_length=100, blank=True)
    link_url2 = models.URLField(blank=True)
    
    main_title = models.CharField(max_length=200)
    main_title2 = models.CharField(max_length=200)
    
    GezilecekYer1 = models.CharField(max_length=200, unique=True,)
    description_1 = models.TextField()
    adreslink1 = models.URLField(blank=True)
    
    
    GezilecekYer2 = models.CharField(max_length=200, unique=True)
    description_2 = models.TextField()
    adreslink2 = models.URLField(blank=True)
    
    GezilecekYer3 = models.CharField(max_length=200, unique=True)
    description_3 = models.TextField()
    adreslink3 = models.URLField(blank=True)
    
    GezilecekYer4 = models.CharField(max_length=200, unique=True)
    description_4 = models.TextField()
    adreslink4 = models.URLField(blank=True)
    
    
    def __str__(self):
        return self.name


class servicic(models.Model):
    
    service_detail = models.ForeignKey(ServiceDetail, related_name='servicics', on_delete=models.CASCADE)
    title1 = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to="media")
    description1 = models.TextField()
    
    title2 = models.CharField(max_length=200)
    image2 = models.ImageField(upload_to="media")
    description2 = models.TextField()
    
    def __str__(self):
        return self.title1