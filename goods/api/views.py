from goods.models import Category, Product, Photo
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CategorySerializer
from .serializers import ProductDetailSerializer
from .serializers import CategoryDetailSerializer
from .serializers import ProductSerializer
from .serializers import PhotoSerializer

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug' # for slug search
    

class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    
    
    
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
class PhototListAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_field='image'