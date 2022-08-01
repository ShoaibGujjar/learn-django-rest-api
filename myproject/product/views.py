from rest_framework.response import Response
from rest_framework import generics,mixins # ,authentication,permissions
from .models import Products
from .serializers import ProductSerializers
from api.permission import IsStaffEditorPermission
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin
# from .paginations import CustomPagination


# class ListModelMixin(object):
#     """
#     List a queryset.
#     """
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             print('shoaib')
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


class ProductListCreateAPIView(
    UserQuerySetMixin,
    generics.ListCreateAPIView,
    StaffEditorPermissionMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializers
    # authentication_classes=[authentication.SessionAuthentication,TokenAuthentication] becaue i define this in setting.py
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)
    
    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     request=self.request
    #     user=request.user
    #     if not user.is_authenticated:
    #         return Products.objects.none()
    #     # print(request)
    #     return qs.filter(user=request.user)
product_list_create_view=ProductListCreateAPIView.as_view()

class ProductDetailAPIView(
    UserQuerySetMixin,
    generics.RetrieveAPIView,
    StaffEditorPermissionMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializers
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

product_detail_view=ProductDetailAPIView.as_view()



class ProductUpdateAPIView(
    UserQuerySetMixin,
    generics.UpdateAPIView,
    StaffEditorPermissionMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializers
    # permission_classes=[permissions.DjangoModelPermissions]
    lookup_field='pk'
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission] #beacue is define permittion mixin in header
    def perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
product_update_view=ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    UserQuerySetMixin,
    generics.DestroyAPIView,
    StaffEditorPermissionMixin):
    queryset=Products.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'
    # permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
product_delete_view=ProductDestroyAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializers

product_List_view=ProductListAPIView.as_view()


class ProductMixinView(
    mixins.ListModelMixin,
    UserQuerySetMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):
    queryset=Products.objects.all()
    serializer_class=ProductSerializers
    lookup_field='pk'
    def get(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # email=serializer.validated_data.pop('email')
        # print(email)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view that doing cool"
        serializer.save(content=content)

product_mixin_view=ProductMixinView.as_view()

@api_view(['GET','POST'])
def product_alt_view(request,pk=None):

    method=request.method
    if method=="GET":
        if pk is not None:
            obj=get_object_or_404(Products,pk=pk)
            data=ProductSerializers(obj,many=False).data
            return Response(data)
        queryset=Products.objects.all()
        data=ProductSerializers(queryset,many=True).data
        return Response(data)

    if method=="POST":
            serializer=ProductSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                title=serializer.validated_data.get('titel')
                content=serializer.validated_data.get('content') or None
                print(content)
                if content is None:
                    print(content)
                    content = title
                serializer.save(content=content)
                # intstance=serializer.save()
                print(serializer.data)  
                return Response(serializer.data)
    return Response({"invlid":"not goog data"})