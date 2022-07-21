from itertools import product
from rest_framework import viewsets,mixins
from .models import Products
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> queryset
    get -> retrive -> product Instance Detail  View
    post -> create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    '''
    queryset=Products.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'

class ProductsGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get -> list -> queryset
    get -> retrive -> product Instance Detail  View
    '''
    queryset=Products.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'

# product_list_view=ProductsGenericViewSet.as_view({'get':'list'})
# product_detail_view=ProductsGenericViewSet.as_view({'get':'retrive'})