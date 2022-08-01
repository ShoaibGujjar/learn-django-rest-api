
from rest_framework.routers import DefaultRouter
from product.viewsets import ProductViewSet,ProductsGenericViewSet

router=DefaultRouter()
router.register('products',ProductsGenericViewSet,
basename='products')
# print(router.urls)
urlpatterns=router.urls

