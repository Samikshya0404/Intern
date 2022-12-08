from django.contrib import admin
from django.urls import path, include
from todoapp import views
from todoapp.views import todoappView,MyView,TodolistView,TodoCreate, TodoUpdate, TodoDetails, deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', todoappView,name="test"),
    path('', TodolistView.as_view()),
    # path('addTodoItem/', addTodoView), 
    path('about/', MyView.as_view()),
    # path('deleteTodoItem/<int:i>/', deleteTodoView), 
    # path('class/list',TodoCreate.as_view(),name="list_view"),
    path('', TodoCreate.as_view() ),
    path('updateTodoItem/<int:i>', TodoUpdate.as_view()),
    path('details/<int:i>', TodoDetails.as_view()),
    path('deleteTodoItem/<int:i>/', deleteTodoView.as_view()),
]
