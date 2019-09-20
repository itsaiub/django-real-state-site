from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('listing/', include('listings.urls', namespace='listings')),
    path('realtors/', include('realtors.urls', namespace='realtors')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
