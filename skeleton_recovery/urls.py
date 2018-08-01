
#import...
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/catalog/')),
    path('accounts/', include('django.contrib.auth.urls')),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)