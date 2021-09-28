from django.db import models

# Create your models here.



class Todo(models.Model):
    titel = models.CharField(max_length=50, verbose_name='Titel')
    completed = models.BooleanField(verbose_name='Status')

    def __str__(self):
        return self.titel