"""blog URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from category import views as CategoryViews
from posts import views as PostsViews
from index import views as IndexView
from pages import views as PageViews

admin.autodiscover()

urlpatterns = [
	url(r'^$', IndexView.index, name='index'),
	url(r'^yazi/(?P<slug>[\w-]+)', PostsViews.detail, name='posts'),
	url(r'^kategoriler/', CategoryViews.home, name='category'),
    url(r'^iletisim/', PageViews.contact, name='iletsim'),
    url(r'^admin/', include(admin.site.urls)),


	url(r'^static/(.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),

] 