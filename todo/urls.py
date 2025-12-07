from django.urls import path
from .views import TodoView

urlpatterns = [
    path("todo/", TodoView.as_view(), name="todo_name"),
    path("todo/<int:pk>/", TodoView.as_view(), name="todo_detail"),
]
