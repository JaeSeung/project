from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=20)
    main_photo = models.ImageField()
    detail_photo = models.ImageField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
# Create your models here.

