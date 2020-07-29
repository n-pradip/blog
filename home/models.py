from django.db import models

# Create your models here.
class contact_us(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact_issue = models.TextField()
    # time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        upper_name = self.name.upper()
        return 'Message from : '+ upper_name
