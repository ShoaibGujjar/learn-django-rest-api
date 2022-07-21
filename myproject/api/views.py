from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from product.models import Products
from product.serializers import ProductSerializers
# Create your views here.

@api_view(["GET","POST"])
def get(request):  
    data=request.data
    print(data) 
    serializer=ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        intstance=serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    # instance=Products.objects.all().order_by("?").first()
    # data={}
    # if instance:
    #     data=ProductSerializers(instance).data 
        # data['id']=model_data.id
        # data['title']=model_data.title
        # data['content']=model_data.content
        # data['price']=model_data.Price

    return Response(data)