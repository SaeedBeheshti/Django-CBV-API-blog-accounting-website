from django.urls import path, re_path, include
from django.views.generic import TemplateView, RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = 'blog'
urlpatterns = [
    path('cbv', views.Indexview.as_view(), name='cbv.test'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('go to maktab/', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhooneh'),
    path('create/', views.Postcreateview.as_view(), name='post-create'),
    path('api/v1/', include('blog.api.v1.urls')),

    # swagger urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
