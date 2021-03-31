
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name = "index" ),
    path('<int:flight_id>', views.flight, name = "flight"),
    path('<int:flight_id>/book', views.book, name = "book")
]
