from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("users.urls", namespace="users")),
    path("post/", include("posts.urls", namespace="posts")),
    path("api-auth/", include("rest_framework.urls")),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
