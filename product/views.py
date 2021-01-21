from django.shortcuts import render
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView,\
     CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import permissions as p, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product, Category, Comment
from .serializers import ProductSerializer, CategorySerializer,\
     CreateUpdateProductSerializer, CommentSerializer, ProductListSerializer
from .filters import ProductFilter


# @api_view(["GET"])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# class ProductList(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)



# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductDetail(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class CreateProduct(CreateAPIView):
#     queryset = Product.objects.all()
#     permission_classes = [p.IsAdminUser]
#     serializer_class = CreateUpdateProductSerializer


# class UpdateProduct(UpdateAPIView):
#     queryset = Product.objects.all()
#     permission_classes = [p.IsAdminUser]
#     serializer_class = CreateUpdateProductSerializer
    

# class DeleteProduct(DestroyAPIView):
#     queryset = Product.objects.all()
#     permission_classes = [p.IsAdminUser]


class MyPagination(PageNumberPagination):
    page_size = 1


class CategoriesList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    ilter_class = ProductFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductSerializer
        elif self.action == 'list':
            return ProductListSerializer
        return CreateUpdateProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'search']:
            permissions = []
        else:
            permissions = [p.IsAdminUser]
        return [permission() for permission in permissions]


    @action(methods=['get'], detail=False)
    def search(self, request):
        q = request.query_params.get('q')
        queryset = self.get_queryset()
        if q is not None:
            queryset = queryset.filter(Q(title__icontains=q)| Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [p.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

















    

