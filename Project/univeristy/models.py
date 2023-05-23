from django.db import models


class Category(models.Model):
    name  = models.CharField(max_length=45)
    def __str__(self) :
        return self.name

class SubCategory(models.Model):
    title = models.CharField(max_length=45, verbose_name='Oyunun Skili')
    link = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='image',null=True, verbose_name='Oyunun IMG')
    description = models.TextField(null=True,verbose_name='Oyunun contenti')
    

    def __str__(self) :
        return self.title