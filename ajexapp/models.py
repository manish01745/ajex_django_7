from django.db import models

class Detail(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=False, null=False)
    
    def __str__(self):
        return self.name


    
