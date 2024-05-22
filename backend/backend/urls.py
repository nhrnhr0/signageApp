"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from core.views import playlist_detail_view,playlist_upload_asset,playlist_delete_asset, PlayListsView
from core.views import screens_view,screen_detail_view,screens_islands_view,screen_display_view
from products.views import find_product_view
from django.conf import settings
from django.conf.urls.static import static
from core.views import test, api_register_screen,redirect_to_display
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    
    path('api/register-screen/', api_register_screen),

    path('playlists/', PlayListsView.as_view(), name='playlists'),
    path('playlists/<str:pk>/', playlist_detail_view, name='playlist-detail'),
    path('playlists/<str:pk>/upload-asset/', playlist_upload_asset, name='playlist-assets'),
    path('playlists/<str:pk>/assets/<str:asset_id>/', playlist_delete_asset, name='playlist-asset-detail'),
    
    path('screens/', screens_view, name='screens'),
    path('screens/<str:pk>/', screen_detail_view, name='screen-detail'),
    path('screens-islands/', screens_islands_view, name='screens-islands'),
    path('screens/display/<str:code>/', screen_display_view, name='screens-display'),
    
    path('products/find/<str:barcode>', find_product_view, name='find-product'),
    path('test/', test, name='test'),
    path('display/', redirect_to_display),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        
    urlpatterns += [
        path('__debug__/', include("debug_toolbar.urls")),
    ]