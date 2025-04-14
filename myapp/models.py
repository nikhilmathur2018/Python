from django.db import models

class ContactUs(models.Model):  
    name = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null=True)  
    phone = models.CharField(max_length=13)
    project = models.CharField(max_length=40)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name  
