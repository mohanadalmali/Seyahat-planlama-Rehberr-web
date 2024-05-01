from django.db import models
class IndexPage(models.Model):
  # Ana sayfa için içerik
  index_title = models.CharField(max_length=200)
  index_image = models.ImageField(upload_to="media")
  index_description = models.TextField()
  # Hakkımızda için içerik
  about_title = models.CharField(max_length=200)
  about_image = models.ImageField(upload_to="media")
  about_description = models.TextField()
  # Neden Bizi Seçmelisiniz için içerik
  why_choose_us_title = models.CharField(max_length=200)
  why_choose_us_description = models.TextField()
  # Footer bilgileri
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
  