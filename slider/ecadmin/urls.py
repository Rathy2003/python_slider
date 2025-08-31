from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path("", views.dashboard, name="ecadmin.dashboard"),
    path("slider/", views.index, name="ecadmin.slider"),
    path("slider/move/<str:id>", views.slider_move, name="ecadmin.slider.move"),
    path("slider/create/", views.create_slider, name="ecadmin.slider.create"),
    path("slider/delete", views.delete_slider, name="ecadmin.slider.delete"),
    path("slider/edit/<str:id>", views.edit_slide, name="ecadmin.slider.edit"),
]