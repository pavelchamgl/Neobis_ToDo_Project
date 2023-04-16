from django.urls import path
from .views import get_todo_list, create, complete, delete, update

app_name = 'todo_app'

urlpatterns = [
    path("", get_todo_list, name="todo_list"),
    path("create", create, name="create"),
    path("complete/<int:todo_id>", complete, name="complete"),
    path("update/<int:todo_id>", update, name="update"),
    path("delete/<int:todo_id>", delete, name="delete"),
]