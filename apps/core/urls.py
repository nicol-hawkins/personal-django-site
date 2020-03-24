from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView
from apps.core import views

urlpatterns = [
    path('', views.about_me, name="about-me"),
    path('about-me', views.about_me, name="about-me"),
    path('my-resume', views.resume, name="my-resume"),
    path('my-projects', views.projects, name="my-projects"),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/img/favicon.ico'))
]

# Boilerplate to include static files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
