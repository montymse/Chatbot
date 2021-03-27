from django.urls import path

from .views import chat_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('chat/<str:room_name>/', chat_view, name='chat'),
]
