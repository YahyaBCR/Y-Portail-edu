from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#notes model
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    #afficher le titre des nptes
    def __str__(self):
        return self.title

    #supprimer s 'notess'
    class Meta:
        verbose_name = "notes"
        verbose_name_plural = "notes"







    
