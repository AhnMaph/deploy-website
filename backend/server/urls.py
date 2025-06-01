from django.contrib import admin
from django.urls import path, include
from manga.views import home
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('audio.urls')),
    path('health/', health_check, name='health_check_slash'),
    path('api/', include('manga.urls')),  # API starts with /api/
    path('api/', include('genres.urls')),  # API starts with /api/
    path('api/', include('users.urls')),
    path('api/', include('chapter.urls')),
    path('api/', include('novel.urls')),
    path('api/', include('forum.urls')),

    path('', home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()