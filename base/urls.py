from django.urls import URLPattern,path
from . import views

urlpatterns=[
    path("",views.home,name="Home")  ,
    path ("nextpage/",views.nextpage ,name="Nextpage")
]