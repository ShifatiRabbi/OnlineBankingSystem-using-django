from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('home/', views.home, name='home'),
    path('', views.home, name='about_us'),
    path('', views.home, name='contact_us'),
    path('', views.home, name='gallery'),
    path('', views.home, name='signup'),
    path('see_all_customers/', views.see_all_customers, name='see_all_customers'),
    path('see_all_transactions/', views.see_all_transactions, name='see_all_transactions'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:customer_id>/', views.update_profile, name='update_customer'),
    path('add_money/<int:customer_id>/', views.add_money, name='add_money'),
    path('delete_customer/<int:customer_id>/', views.delete_customer, name='delete_customer'),
    

    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    #path('update_profile/', views.update_profile, name='update_profile'),
    path('transaction_details/<int:customer_id>/', views.customer_transaction, name='transaction_details'),
    path('money_transfer/', views.money_transfer, name='money_transfer'),
    path('chat_with_admin/', views.chat_with_admin, name='chat_with_admin'),

    # Add more URL patterns for other functionalities if needed
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('custom_login/', views.custom_login, name='custom_login'),

    path('inbox/', views.inbox, name='inbox'),
    path('sentbox/', views.sentbox, name='sentbox'),
    path('send_message/<slug:username>/', views.send_message, name='send_message'),
]
