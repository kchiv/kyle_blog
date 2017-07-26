from django.conf.urls import url
from . import views

app_name = 'pages'

urlpatterns = [
	url(r'^(?P<slug>[-\w]+)/$', views.single_page, name='single_page'),
]