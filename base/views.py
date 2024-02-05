import re
from django.shortcuts import render
from django.http import HttpResponse

rooms=[
    { 'id' :1 , 'name':"Python room" },
    { 'id' :2 , 'name':"C room" },
    { 'id' :3 , 'name':"C++ room" },
    { 'id' :4 , 'name':"Java room" }
]


def home(request):
    context={'rooms':rooms}
    return render(request,'base/home.html',context)
def room(request,id):
    room=None
    for i in rooms:
        if i['id'] == int(id):
            room=i
    context = { 'room':room}
    return render(request,'base/room.html',context)
