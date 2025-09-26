from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter
from .paginations import LargeResultsSetPagination
'''
                                !!!Function based views(this is my first version of coding!) !!!

from rest_framework.decorators import api_view, permission_classes

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def Postlist(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET','PUT','DELETE'])
def Postdetail(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return Response({'message': 'post has been deleted'}, status=204)
'''
"""
                                               # POSTDETAIL class without generics and mixins
class Postdetail(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, id):
        post = get_object_or_404(self.get_queryset(), id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = get_object_or_404(self.get_queryset(), id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id):
        post = get_object_or_404(self.get_queryset(), id=id)
        post.delete()
        return Response({'message': 'post has been deleted'}, status=204)
"""
# ====================== GenericAPIView Version ======================

# class Postlist(ListCreateAPIView):
#     """Getting a list of posts and creating new posts"""
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)

#=====================================================================
# class Postdetail(RetrieveUpdateDestroyAPIView):
#     pass
# """Retrieve, update, delete a specific post"""
# permission_classes = [IsAuthenticated]
# serializer_class = PostSerializer
# queryset = Post.objects.filter(status=True)

#======================VIEWSET API===============================================

class PostViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filterset_fields = ('author', 'status')
    pagination_class = LargeResultsSetPagination

class CategoryModelViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


