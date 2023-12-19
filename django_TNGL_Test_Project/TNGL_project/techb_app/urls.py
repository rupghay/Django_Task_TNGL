from django.urls import path
from techb_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.customer_list, name='customer_list'),
    path('create/', views.create_customer, name='create_customer'),
    path('update/<int:customer_id>/', views.update_customer, name='update_customer'),
    path('delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),
]
