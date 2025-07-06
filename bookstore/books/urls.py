from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.book_list), name='book_list'),  # ✅ force login
    path('books/', login_required(views.book_list)),              # optional alias
    path('add/', login_required(views.add_book), name='add-book'),
    path('edit/<int:id>/', login_required(views.edit_book), name='edit-book'),
    path('delete/<int:id>/', login_required(views.delete_book), name='delete-book'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
