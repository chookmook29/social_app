from django.shortcuts import render
from .models import UserMessage
from user.models import CustomUser


def user_messages(request, pk):
    user = CustomUser.objects.get(pk=pk)
    message_list = UserMessage.objects.select_related().filter(recipient=pk).order_by('-date')
    return render(request, 'messages.html', {'user': user, 'message_list': message_list})
