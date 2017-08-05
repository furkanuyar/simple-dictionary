from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^simple_dictionary/$', views.dictionary, name='simple_dictionary')
]
