from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import index, blog, post, contact, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact/', contact),
    path('about/', about),
    path('blog/', blog, name='post-list'),
    path('post/<slug>/', post, name='post-detail'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
