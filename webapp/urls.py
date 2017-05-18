from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^contact/$',views.contact, name='contact'),
	url(r'^page2.html',views.page2, name='page2'),]
