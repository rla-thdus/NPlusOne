from django.urls import path

from . import views

urlpatterns = [
    path('one-to-one', views.TestAPI.as_view()),
]