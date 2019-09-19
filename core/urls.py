from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('listing/', include('listings.urls', namespace='listings')),
    path('realtors/', include('realtors.urls', namespace='realtors')),
]
