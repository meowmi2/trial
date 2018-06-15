from django.conf.urls import url
from DefectsNotification import views

app_name = 'basic_app'

urlpatterns = [
    #url(r'^$', views.AddressFormView, name='summary'),
    #url(r'^$', views.index.as_view(), name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
]
