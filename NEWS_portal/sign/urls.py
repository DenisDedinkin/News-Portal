from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndexView, BaseRegisterView, upgrade_me

urlpatterns = [
    path('', IndexView.as_view()),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', BaseRegisterView.as_view(template_name='register.html'), name='register'),

    path('upgrade/', upgrade_me, name='upgrade')
]