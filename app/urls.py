from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('api/send-email/', views.send_email, name='send_email'),
]