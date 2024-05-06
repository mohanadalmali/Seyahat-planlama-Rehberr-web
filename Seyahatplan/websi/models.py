from django.db import models
class IndexPage(models.Model):
  about_title = models.CharField(max_length=200)
  about_image = models.ImageField(upload_to="media")
  about_description = models.TextField()
  why_choose_us_title = models.CharField(max_length=200)
  why_choose_us_description = models.TextField()
  why_choose_us_image = models.ImageField(upload_to="media", blank=True, null=True)
  
  
  footer_instagram_link = models.URLField(max_length=200, blank=True, null=True)
  footer_facebook_link = models.URLField(max_length=200, blank=True, null=True)
  footer_linkled_link = models.URLField(max_length=200, blank=True, null=True)
  footer_X_link = models.URLField(max_length=200, blank=True, null=True)
  footer_phone_number = models.CharField(max_length=20, blank=True, null=True)
  footer_email = models.EmailField(max_length=254, blank=True, null=True)
  def __str__(self):
    return "Ana Sayfa"

class abouts(models.Model):
  about_titleb=models.CharField(max_length=200)
  about_imageb = models.ImageField(upload_to="media")
  about_descriptionb = models.TextField()
  def __str__(self):
    return "blok sayfasi"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
