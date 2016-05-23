from django.db import models



CATEGORY_CHOICES = (
    		('TOP' , 'top'),
    		('BOTTOM' , 'bottom'),
    		('CODY' , 'cody'),
    	)




class Product(models.Model):
    title = models.CharField(max_length=20)
    main_photo = models.ImageField()
    detail_photo = models.ImageField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cloth_category = models.CharField(max_length=6, choices = CATEGORY_CHOICES, default='CODY')
   

    def __str__(self):
        return self.title

class Product_top(models.Model):
    title = models.CharField(max_length=20)
    main_photo = models.ImageField()
    detail_photo = models.ImageField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cloth_category = models.CharField(max_length=6, choices = CATEGORY_CHOICES, default='CODY')


    def __str__(self):
        return self.title



class Product_bottom(models.Model):
    title = models.CharField(max_length=20)
    main_photo = models.ImageField()
    detail_photo = models.ImageField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cloth_category = models.CharField(max_length=6, choices = CATEGORY_CHOICES, default='CODY')


    def __str__(self):
        return self.title
