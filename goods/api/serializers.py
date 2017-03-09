from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField
from rest_framework.serializers import StringRelatedField, PrimaryKeyRelatedField 
from goods.models import Category, Product, Photo, Brand

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        
class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'parent', 'description')
        
        
class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'slug')
        
     
class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    class Meta:
        model = Product
        fields = ('id', 'category', 'brand', 'name',
         'price', 'is_available')
        
       
class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ('image', 'is_active')
        
        
class ProductDetailSerializer(ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    photos = PhotoSerializer(many=True, read_only=True )
    # print('img', images)
    class Meta:
        model = Product
        fields = ('id', 'category', 'brand', 'name',
        'description', 'price', 'is_available', 'created', 'photos')