from django.db import models

# Create your models here.
class Post(models.Model):
    serial_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=5000)
    aurthor = models.CharField(max_length=20)
    timestamp = models.DateTimeField(blank=True)
    slug = models.CharField(max_length=150)
    media_image = models.ImageField(upload_to='blog/images',default='')
    # time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
