from django.urls import path
from . import views
app_name = 'hostels'

urlpatterns = [
    path('listings/', views.hostel_list, name='list'),
]
