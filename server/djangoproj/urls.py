"""djangoproj URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about/', RedirectView.as_view(url='/static/About.html', permanent=False)),
    path('contact/', RedirectView.as_view(url='/static/Contact.html', permanent=False)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
