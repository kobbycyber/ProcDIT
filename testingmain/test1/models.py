from django.db import models

# Create your models here.
class Post(models.Model):
   postcontext = models.TextField()
   catalogue = models.TextField(max_length=40)
   description = models.TextField()
   posttitle = models.TextField(max_length=256,blank=False)
   createdat = models.TextField()
   urlimg = models.URLField()
   posturl =models.URLField()
   def __str__(self):
       return self.posttitle[:50]
    