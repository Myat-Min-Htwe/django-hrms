from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.attendance_list, name='attendancelist'),
    path('create/', views.attendance_create, name='create'),
    path('detail/<int:pk>/', views.attendance_detail, name='detail'),
    path('update/<int:pk>/', views.attendance_update, name='update'),
    path('delete/<int:pk>/', views.attendance_delete, name='delete'),

    path('search_by/',views.search_by),
    path('order_by/',views.order_by),
]