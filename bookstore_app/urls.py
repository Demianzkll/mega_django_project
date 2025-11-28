
from django.urls import path
from . import views
urlpatterns = [
    path('infinitive/', views.infinitive),
    path('books/', views.BookListView.as_view(), name='book-list'),
    # path('books2/', views.book_list),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/new/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
]
