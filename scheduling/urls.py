from django.contrib import admin
from django.urls import path, include
from scheduling import views



urlpatterns = [
    path("", views.ServiceList.as_view()),
    path("<int:pk>/", views.ServiceDetailView.as_view())

]