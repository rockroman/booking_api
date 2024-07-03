from django.contrib import admin
from django.urls import path, include
from booking import views



urlpatterns = [
    path("", views.BookingListCreateAPIView.as_view()),
    # path("<int:pk>/", views.ServiceDetailView.as_view())

]