from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class Menu(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='imagesMenu')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



# Create your models here.
