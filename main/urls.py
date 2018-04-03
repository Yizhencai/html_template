from django.urls import path

from . import views

urlpatterns = [
    path('/index', views.index, name = 'index'),
    path('/contact', views.contact, name = 'contact'),
    path('/about', views.about, name = 'about'),
    path('/portfolio_detail', views.portfolio_detail, name = 'portfolio_detail'),
    path('/work', views.work, name = 'work')
]
