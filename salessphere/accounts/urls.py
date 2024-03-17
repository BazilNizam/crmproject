from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('create_lead/', views.create_lead, name='create_lead'),
    path('leads/', views.index, name='leads'),
    path('update_lead/<id>', views.update_lead, name='update_lead'),
    path('delete_lead/<id>', views.delete_lead, name='delete_lead'),

    path('create_opportunity/', views.create_opportunity, name='create_opportunity'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('update_opportunity/<id>', views.update_opportunity, name='update_opportunity'),
    path('delete_opportunity/<id>', views.delete_opportunity, name='delete_opportunity'),

    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_complete'),
]
