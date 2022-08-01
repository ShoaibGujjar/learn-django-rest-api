<<<<<<< HEAD
from unittest import result
from rest_framework import generics
from rest_framework.response import Response
from product.models import Products
from product.serializers import ProductSerializers

from . import client
class SearchListView(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        user=None
        if request.user.is_authenticated:
            user=request.user.username
        query=request.GET.get('q')
        tag=request.GET.get('tag') or None
        public=str(request.GET.get('public'))!="0"
        # print(user,query,public,tag)
        if not query:
            return Response('',status=400)
        results=client.perform_search(query,tags=tag ,user=user,public=public)
        return Response(results)
class SearchListOldView(generics.ListAPIView):
=======
from rest_framework import generics

from product.models import Products
from product.serializers import ProductSerializers

class SearchListView(generics.ListAPIView):
>>>>>>> b28fc7cfec149e4204727cf1f32a9f8ae9b77e26
    queryset = Products.objects.all()
    serializer_class = ProductSerializers

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q")
        results = Products.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results
