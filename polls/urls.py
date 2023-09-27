from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello/", views.post_call, name="post_call"),
    path("srini/", views.put_call, name="put_call"),
    path("rikesh/", views.delete_call, name="delete_call"),
    path("ok/", views.PostMan.as_view()),
]