<<<<<<< HEAD
import random
=======
>>>>>>> b28fc7cfec149e4204727cf1f32a9f8ae9b77e26
from django.db import models
from django.conf import settings
from django.db.models import Q
User=settings.AUTH_USER_MODEL 

# Create your models here.
<<<<<<< HEAD

TAGE_MODEL_VALUES=['electronice','cars','boats','movies','cameras']
=======
>>>>>>> b28fc7cfec149e4204727cf1f32a9f8ae9b77e26
class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)
class   Products(models.Model):
    user=models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    Price=models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    public=models.BooleanField(default=True)

    objects= ProductManager()
<<<<<<< HEAD
    def is_public(self)->bool:
        return self.public # true or false
    
    def get_tags_list(self):
        return[random.choice(TAGE_MODEL_VALUES)]
=======
>>>>>>> b28fc7cfec149e4204727cf1f32a9f8ae9b77e26
    @property
    def sale_price(self):
        return "%.2f" %(float(self.Price)*0.8)
    
    def get_discount(self):
        return "122"
<<<<<<< HEAD
    
    def __str__(self):
        return f"{self.title}"
    
=======
>>>>>>> b28fc7cfec149e4204727cf1f32a9f8ae9b77e26

