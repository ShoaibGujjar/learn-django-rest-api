from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL 

# Create your models here.
class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    def search(self,query,user=None):
        return self.filter(title_icontains=query)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)
    def search(self,query,user=None):
        return self.get_queryset().is_public().search(query,user=user)
class   Products(models.Model):
    user=models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    Price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    public=models.BooleanField(default=True)
    @property
    def sale_price(self):
        return "%.2f" %(float(self.Price)*0.8)
    
    def get_discount(self):
        return "122"

