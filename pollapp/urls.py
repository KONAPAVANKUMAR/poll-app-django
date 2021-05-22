from django.urls import path
from .views import *

urlpatterns = [

    path('',pollview,name ='pollspage'),
    path('upvote/<int:id>/',upvote,name = "upvote"),
    path('downvote/<int:id>/',downvote,name = "downvote"),


]