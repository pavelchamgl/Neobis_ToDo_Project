from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import ToDo


# Вывод всех не выполненных заданий
def get_todo_list(request):
    context = {"todo_list": ToDo.objects.filter(is_complete=False).order_by('deadline')}
    return render(request, "todo_app/todo_list.html", context)


# Добавление нового задания
@require_http_methods(["POST"])
@csrf_exempt
def create(request):
    title = request.POST["title"]
    description = request.POST["description"]
    deadline = request.POST["deadline"]
    todo = ToDo(title=title, description=description, deadline=deadline)
    todo.save()
    messages.success(request, 'Задача успешно создана!')
    # Redirect на страницу с которой был отправлен запрос
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Зедактирование задания
def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.deadline = request.POST['deadline']
        todo.save()
        messages.success(request, 'Задача изменена!')
        return redirect('todo_app:todo_list')
    context = {'todo': todo}
    return render(request, 'todo_app/update.html', context)


# Изменения статуса задания на "выполнено"
def complete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    messages.success(request, 'Задача успешно выполнена!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Удаление задания из БД
def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, 'Задача удалена!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
