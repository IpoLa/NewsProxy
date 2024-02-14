from django.contrib import admin
from django.urls import path
from news_proxy_app import views

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="News Proxy API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', views.init_articles),
    path('articles/<int:id>', views.getArticleById, name='article_by_id'),
    
    path('articles/categories/', views.init_categories),
    path('articles/category/<int:category_id>/', views.articles_by_category, name='articles_by_category'),
    path('articles/category/<str:category_name>/', views.articles_by_category_name, name='articles_by_category_name'),

    path('articles/sources/', views.init_sources),
    path('articles/source/<int:source_id>/', views.articles_by_source, name='articles_by_source'),
    path('articles/source/<str:source_name>/', views.articles_by_source_name, name='articles_by_source_name'),
    
    path('articles/country/<str:country_code>/', views.articles_by_country, name='articles_by_country'),
    path('articles/search/', views.search_articles, name='search_articles'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
