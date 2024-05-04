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
    
    main_title1 = models.CharField(max_length=200)
    title1 = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to="media")
    description1 = models.TextField()
    
    main_title2 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    image2 = models.ImageField(upload_to="media")
    description2 = models.TextField()
    
    def __str__(self):
        return self.title
