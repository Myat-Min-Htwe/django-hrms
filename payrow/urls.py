from django.urls import path
from . import views


urlpatterns = [
    path('list/',views.payrow_list),
    path('create/',views.payrow_create),
    path('detail/<int:pk>/',views.payrow_detail),
    path('update/<int:pk>/',views.payrow_update),
    path('delete/<int:pk>/',views.payrow_delete),

    path('search_by/',views.search_by),
    path('order_by/',views.order_by),
]