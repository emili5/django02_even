from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

app_name="vote"
urlpatterns=[
    path('index/',views.index,name="index"),
    path('detail/<bpk>',views.detail,name='detail'),
    path('vote/<tpk>',views.vote,name="vote")
]