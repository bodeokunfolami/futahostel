from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('application/', views.hostel_app, name='app'),
    path('application/<int:id>/', views.hostel_app_detail, name='app_detail'),
    path('change_password/', PasswordChangeView.as_view(template_name='users/change_password.html', success_url=reverse_lazy('users:change_password')), name="change_password"),
    path('edit_profile/', views.edit_pofile, name='edit_profile')
]