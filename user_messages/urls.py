from django.urls import path
from . import views

urlpatterns = [
   path('messages/<int:pk>', views.user_messages, name='user_messages'),
]
