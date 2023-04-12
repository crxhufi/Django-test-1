from django.conf import settings
from django.db import models
from django.utils import timezone


class QR(models.Model):
    image = models.ImageField(upload_to='qr/')  

    published_date = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.image.name


# Create your models here.
