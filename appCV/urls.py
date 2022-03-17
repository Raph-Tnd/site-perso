from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home),
    re_path(r'^features/$', views.features),
    re_path(r'^features/CV/$',views.CV),
    re_path(r'^features/CV/files/CV.pdf/$',views.DL),
    re_path(r'^contact/$', views.contact),
]
