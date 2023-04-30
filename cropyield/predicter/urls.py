from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.predicter, name='predicter'),
    path('result',views.Forminfo, name='result')
]
