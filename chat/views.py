import random
import string

from django.shortcuts import render, redirect
from .models import Room
from .form import RoomForm


# Create your views here.
def home_view(request):

    form = RoomForm(request.POST or None)

    if form.is_valid():
        p = Room(
            room_name=get_room_string(),
            user_name=form.cleaned_data.get('navn')
        )
        p.save()
        return redirect(p.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, "home.html", context)


def chat_view(request, room_name):
    room = Room.objects.filter(room_name=room_name)
    if room.exists():
        if request.GET.get('LeaveChat'):
            Room.objects.filter(room_name=room_name).delete()
            return redirect('/')

        context = {
            'user_name': room[0].user_name,
            'room_name': room_name,
        }
        return render(request, "chatroom.html", context)
    else:
        return redirect('/')


def get_room_string():
    room_string = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    if Room.objects.filter(room_name=room_string).exists():
        get_room_string()
    else:
        return room_string