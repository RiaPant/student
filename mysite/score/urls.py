from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
   # url(r'^score/', include('score.urls')),
   # url(r'^fill/$', views.fill, name="fill"),
    url(r'^results/$', views.results, name="results"),
    url(r'^create/$', views.create, name="create"),
]