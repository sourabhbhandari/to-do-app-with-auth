from django.urls import path

from django.views.generic.list import ListView
from .views import TaskList,TaskDetail, TaskCreate, TaskUpdate, DeleteView, CustomLoginView


urlpatterns = [

    path('login/',CustomLoginView.as_view(), name="login"),

    path('',TaskList.as_view(),name="Tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(),name="task"),
    path('create-task/',TaskCreate.as_view(),name="task-create"),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name="task-update"),
    path('task-delete/<int:pk>/',DeleteView.as_view(),name="task-delete"),
]