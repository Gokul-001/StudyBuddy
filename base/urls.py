from django.urls import URLPattern,path
from . import views

urlpatterns=[
    path("",views.home,name="Home")  ,
    path ("room/<int:id>/",views.room ,name="room")
]