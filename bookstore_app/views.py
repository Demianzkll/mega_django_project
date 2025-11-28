from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse
from .forms import UserRegisterForm
import time
# Create your views here.
from .models import Book

# Create your views here.
class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
    
class BookCreateView(generic.CreateView):
    model = Book
    success_url = '/bookstore/books/'
    fields = ['title', 'author', 'published_date']

class BookDeleteView(generic.DeleteView):
    model = Book
    success_url = '/bookstore/books/'
    
class BookUpdateView(generic.UpdateView):
    model = Book
    success_url = '/bookstore/books/'
    fields = "__all__"
    
    
# def book_list(request):
#     return render(request, 
#                   "bookstore_app/book_list.html", 
#                   {"book_list": Book.objects.all(),
#                    "book_list_page_title" : "Here is list of available books:"})

def infinitive(request):
    while(True):
        time.sleep(1)

def register(request):
    if (request.method == "POST"):
        form = UserRegisterForm(request.POST)
        if (form.is_valid):
            user = form.save(commit=False)

            user = User(username = form.cleaned_data["username"], 
                        email = form.cleaned_data["email"], 
                        first_name = form.cleaned_data["first_name"])

            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect(reverse('book-list'))
        else:
            return render(request, "registration/register_form.html", {"form": form})
    else:
        form = UserRegisterForm()
        return render(request, "registration/register_form.html", {"form": form})
    