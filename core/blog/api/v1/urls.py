from django.urls import path, include
# from .views import Postlist
from . import views
from rest_framework.routers import DefaultRouter
app_name='api-v1'

router = DefaultRouter()
router.register('post', views.PostViewset,basename='posts')
router.register('category', views.CategoryModelViewset,basename='category')
urlpatterns =router.urls

#+======================================================================+
# urlpatterns = [
    # path('post/',Postlist, name='post-list'),


    # path('post/',views.Postlist.as_view(),name='post-list'),
    # path('post/<int:pk>/',views.Postdetail.as_view(),name='post-detail'),
#     path('post/',views.PostViewset.as_view({'get': 'list','post':'create'}),name='post-list'),
#     path('post/<int:pk>/',views.PostViewset.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='post-retrieve'),
#
# ]

