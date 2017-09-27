from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login', views.login, name = 'login'),
    url(r'^create', views.create, name = 'create'),
    url(r'^dashboard', views.dashboard, name = 'dashboard'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^', views.index, name = 'index'),
]