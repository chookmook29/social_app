from django.shortcuts import render


def user_messages(request):
    return render(request, 'messages.html')
