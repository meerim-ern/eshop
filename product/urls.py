from django.urls import path, include
# from .views import #ProductList, ProductDetail, CategoriesList, CreateProduct,\
#     UpdateProduct, DeleteProduct
from .views import ProductViewSet, CategoriesList
from rest_framework.routers import  DefaultRouter

products = ProductViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'post': 'create',
    'delete': 'destroy',
    'get': 'retrieve'

})

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    # path('', ProductList.as_view()),
    # path('detail/<str:pk>/', ProductDetail.as_view()),
    path('categories/', CategoriesList.as_view()),
    # path('create/', CreateProduct.as_view()), 
    # path('update/<str:pk>/', UpdateProduct.as_view()),
    # path('delete/<str:pk>/', DeleteProduct.as_view()),


    # path('', products),
    # path('<str:pk>/', products)

    path('', include(router.urls))

    
]