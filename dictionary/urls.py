from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^simple_dictionary/$', views.get_results, name='simple_dictionary')
]
