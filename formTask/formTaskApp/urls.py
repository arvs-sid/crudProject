from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.formFunc,name='create'),
    path('viewList',views.viewlist,name='view'),
    path('delete/<str:listName>',views.delete,name='delete'),
    path('update/<str:listName>',views.update,name='update'),
]