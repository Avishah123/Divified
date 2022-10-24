from django.contrib import admin
from django.urls import path
from . import views
from .views import *
from django.contrib import admin
from . import views
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('enduser', views.organizer.as_view(), name='enduser'),
    path('stock', views.event_view, name='stock'),
    path('login', auth_views.LoginView.as_view(
        template_name='dashboard/login1.html'), name='login'),
    path('test', views.form_rendering_test, name='test'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete/<stock_id>',views.delete,name='delete'),
    path('new-index',dash_index,name='new-index'),
    path('new-login',dash_login,name='new-login'),
    path('new-register',dash_register,name='new-register'),
    path('new-landing',new_landing,name='new_landing'),
    
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password_reset_form.html',
             subject_template_name='commons/password_reset_subject.txt',
             email_template_name='commons/password_reset_email.html',
           
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
    
     path('chart-home', views.HomeView.as_view()),
    # path('test-api', views.get_data),
    path('charts', views.ChartData.as_view()),
    path('images-new', views.upload, name='images-new'),
    path('dividend-analysis', views.upload_view, name='dividend-analysis'),
    path('dividend-history',test_history,name='dividend-history'),
    path('view/<Stock_ticker>',views.hist_view,name='hist_view'),
    path('face_con',views.face_con,name='face_con'),
    
   
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)