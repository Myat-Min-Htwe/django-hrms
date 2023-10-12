from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.extant_list,name='list'),
    path('create/',views.extant_create,name='create'),
    path('detail/<int:pk>/',views.extant_detail,name='detail'),
    path('update/<int:pk>/',views.extant_update,name='update'),
    path('delete/<int:pk>/',views.extant_delete,name='delete'),

    path('search_by/',views.search_by),
    path('order_by/',views.order_by),
]