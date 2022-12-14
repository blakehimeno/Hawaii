
from django.contrib import admin
from django.urls import path, include
from leads.views import home_page
from django.conf import settings 
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path("__reload__/", include("django_browser_reload.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

