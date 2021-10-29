from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from galapp.views import PictureViewSet
from galleryconfig import settings


router = SimpleRouter()

router.register(r'picture', PictureViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)