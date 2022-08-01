
from rest_framework.routers import DefaultRouter
from product.viewsets import ProductViewSet,ProductsGenericViewSet

router=DefaultRouter()
router.register('products',ProductsGenericViewSet,
basename='products')
<<<<<<< HEAD
# print(router.urls)
=======
print(router.urls)
>>>>>>> b28fc7cfec149e4204727cf1f32a9f8ae9b77e26
urlpatterns=router.urls

