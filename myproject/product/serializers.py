
from wsgiref.validate import validator
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Products
from .validators import validate_title,validate_title_on_hello,unique_product_title
from api.serializers import UserPublicScrializer


class ProductInSelializer(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk',read_only=True)
    title=serializers.CharField(read_only=True)

class ProductSerializers(serializers.ModelSerializer):

    owner=UserPublicScrializer(source='user')
    # related_product=ProductInSelializer(source='user.products_set.all',read_only=True,many=True)
    # my_user_data=serializers.SerializerMethodField(read_only=True)
    # my_discount=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.SerializerMethodField(read_only=True)
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')
    # email=serializers.EmailField(write_only=True)
    title=serializers.CharField(validators=[validate_title_on_hello,unique_product_title])
    # name=serializers.CharField(source='title',read_only=True)
    class Meta:
        model=Products
        fields=[
            'pk',

            # 'owner',

            'owner',
            'url',
            'edit_url',
            'title',
            'content',
            'Price',
            'sale_price',
        ]

    # def get_my_user_data(self,obj):
    #     return{
    #         "username":obj.user.username
    #     }  
    
    # def validate_title(self,value):
    #     qs=Products.objects.filter(title__iexact=value)
    #     print(qs)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value
    def get_edit_url(self,obj):
    # return f"/api/products/{obj.pk}/"
        request=self.context.get('request') #self.request
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
    
    # def create(self, validated_data):
    #     email=validated_data.pop('email')
    #     obj=super().create(validated_data)
    #     #print(email,obj)
    #     return obj
    #     #return Product.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     # instance.title=validated_data.get('title')
    #     # return instance
    #     email=validated_data.pop('email')
    #     return super().update(instance, validated_data)



    # def get_my_discount(self,   obj):
    #     # print(obj.id)
    #     return obj.get_discount()