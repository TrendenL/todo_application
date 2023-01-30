from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Todo
from .form import TodoForm, CustomUserCreationForm


# Signup
class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

# List Todos
class TodosListView(LoginRequiredMixin ,generic.ListView):
    template_name = "todo/todos.html"
    context_object_name = "todos"
    
    def get_queryset(self):
        request_user_userprofile = self.request.user.userprofile
        return Todo.objects.filter(userprofile=request_user_userprofile)
    

# def todos_list(request):
#     todos = Todo.objects.all()
#     context = {
#         "todos": todos
#     }
#     return render(request, "todos.html", context)

# Detail Todo
class TodoDetailView(generic.DetailView):
    template_name = "todo/todo.html"
    queryset = Todo.objects.all()
    context_object_name = "todo"

# def todo_detail(request, pk):
#     todo = Todo.objects.get(id=pk)
#     context = {
#         "todo": todo
#     }
#     return render(request, "todo.html", context)

# Create Todo
class TodoCreateView(generic.CreateView):
    template_name = "todo/todo_create.html"
    form_class = TodoForm

    def get_success_url(self):
        return reverse("todos:todo_list")

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.userprofile = self.request.user.userprofile
        todo.save()
        return super(TodoCreateView, self).form_valid(form)

# def todo_create(request):
#     form = TodoForm()
#     if request.method == "POST":
#         form = TodoForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect("/todos")
    
#     context = {
#         "form": form
#     }
#     return render(request, "todo_create.html", context)

# Update Todo
class TodoUpdateView(generic.UpdateView):
    template_name = "todo/todo_update.html"
    queryset = Todo.objects.all()
    form_class = TodoForm

    def get_success_url(self):
        return reverse("todos:todo_list")

# def todo_update(request, pk):
#     todo = Todo.objects.get(id=pk)
#     form = TodoForm(instance=todo)
#     if request.method == "POST":
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid:
#             form.save()
#             return redirect("/todos")
    
#     context = {
#         "form": form
#     }
#     return render(request, "todo_update.html", context)

# Delete Todo
class TodoDeleteView(generic.DeleteView):
    template_name = "todo/todo_delete.html"
    queryset = Todo.objects.all()

    def get_success_url(self):
        return reverse("todos:todo_list")

# def todo_delete(request, pk):
#     todo = Todo.objects.get(id=pk)
#     todo.delete()
#     return redirect("/todos")

# Completed Todos
class TodoCompletedView(generic.ListView):
    template_name = "todo/todo_completed.html"

    def get_queryset(self):
        request_user_userprofile = self.request.user.userprofile
        return Todo.objects.filter(userprofile=request_user_userprofile, completed=True)

    context_object_name = "completed_todos"

# Active Todos
class TodoActiveView(generic.ListView):
    template_name = "todo/todo_active.html"

    def get_queryset(self):
        request_user_userprofile = self.request.user.userprofile
        return Todo.objects.filter(userprofile=request_user_userprofile, completed=False)

    context_object_name = "active_todos"