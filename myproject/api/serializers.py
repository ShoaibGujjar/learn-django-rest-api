from rest_framework import serializers

class UserProductInSelializer(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk',read_only=True)
    title=serializers.CharField(read_only=True)

class UserPublicScrializer(serializers.Serializer):
    username=serializers.CharField(read_only=True)
    id=serializers.ImageField(read_only=True)
    # other_product=serializers.SerializerMethodField(read_only=True)
    # def get_other_product(self,obj):
    #     # request=self.context.get('request')
    #     print(obj)
    #     user=obj
    #     my_products_qs=user.products_set.all()[:5]
    #     return UserProductInSelializer(my_products_qs,many=True,context=self.context).data

