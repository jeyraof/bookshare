"""bookshare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from bookshare import views as bookshare_views

main_patterns = [
    url(r'^$', bookshare_views.main, name='main'),
]

urlpatterns = [
    url(r'', include(main_patterns)),
    url(r'^book/', include('book.urls', namespace='book')),

    url(r'^logout/',
        'django.contrib.auth.views.logout',
        {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.NODE_MODULES_URL, document_root=settings.NODE_MODULES_ROOT)
