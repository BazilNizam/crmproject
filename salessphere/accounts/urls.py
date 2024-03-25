from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('create_lead/', views.create_lead, name='create_lead'),
    path('leads/', views.index, name='leads'),
    path('update_lead/<id>', views.update_lead, name='update_lead'),
    path('delete_lead/<id>', views.delete_lead, name='delete_lead'),

    path('lead_detail/<id>', views.lead_detail_view, name='lead_detail'),

    path('lead_detail/<id>/calls/', views.calls, name='calls'),
    path('lead_detail/<id>/calls/update/<call_id>/', views.update_call, name='update-call'),
    path('lead_detail/<id>/calls/delete/<call_id>/', views.delete_call, name='delete-call'),
    path('lead_detail/<id>/calls/add/', views.create_call, name='create_call'),

    path('lead_detail/<id>/meetings/', views.meetings, name='meetings'),
    path('lead_detail/<id>/meetings/update/<meeting_id>/', views.update_meeting, name='update-meeting'),
    path('lead_detail/<id>/meetings/delete/<meeting_id>/', views.delete_meeting, name='delete-meeting'),
    path('lead_detail/<id>/meetings/add/', views.create_meeting, name='create_meeting'),

    path('lead_detail/<id>/contacts/', views.contacts, name='contacts'),
    path('lead_detail/<id>/contacts/update/<contact_id>/', views.update_contact, name='update-contact'),
    path('lead_detail/<id>/contacts/delete/<contact_id>/', views.delete_contact, name='delete-contact'),
    path('lead_detail/<id>/contacts/add/', views.create_contact, name='create_contact'),

    path('create_opportunity/', views.create_opportunity, name='create_opportunity'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('update_opportunity/<id>', views.update_opportunity, name='update_opportunity'),
    path('delete_opportunity/<id>', views.delete_opportunity, name='delete_opportunity'),

    path('customers/', views.customers, name='customers'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('update_customer/<id>', views.update_customer, name='update_customer'),
    path('delete_customer/<id>', views.delete_customer, name='delete_customer'),

    path('products/', views.product, name='products'),
    path('create_product/', views.create_product, name='create_product'),
    path('update_product/<id>', views.update_product, name='update_product'),
    path('delete_product/<id>', views.delete_product, name='delete_product'),

    path('create_order/<id>', views.create_order, name='create_order'),
    path('update_order/<id>', views.update_order, name='update_order'),
    path('delete_order/<id>', views.delete_order, name='delete_order'),

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
