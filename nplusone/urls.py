from django.urls import path

from . import views

urlpatterns = [
    path('own-field', views.own_field_test),
    path('one-to-one', views.one_to_one_test),
    path('one-to-many', views.one_to_many_test),
    path('many-to-many', views.many_to_many_test),
]