from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from unicodedata import category

from ...models import Post,Category

class PostSerializer(serializers.ModelSerializer):
    snippet=serializers.ReadOnlyField(source='get_snippet')
    relative_urls=serializers.URLField(source='get_absolute_urls',read_only=True)


    class Meta:
        model = Post
        fields =['id','author','title','content','snippet','category','relative_urls','status','created_date','updated_date']
        read_only_fields=['author']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
