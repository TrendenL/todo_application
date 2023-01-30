from django.urls import path
from todo.views import (
    TodosListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompletedView,
    TodoActiveView
)

app_name = "todos"

urlpatterns = [
    path("", TodosListView.as_view(), name="todo_list"),
    path("active/", TodoActiveView.as_view(), name="todo_active"),
    path("completed/", TodoCompletedView.as_view(), name="todo_complete"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("create/", TodoCreateView.as_view(), name="todo_create"),
    path("<int:pk>/edit/", TodoUpdateView.as_view(), name="todo_update"),
    path("<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete")
]