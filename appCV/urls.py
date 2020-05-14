from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^features/$', views.features),
    url(r'^features/CV/$',views.CV),
    url(r'^features/CV/files/CV.pdf/$',views.DL),
    url(r'^contact/$', views.contact),
]
