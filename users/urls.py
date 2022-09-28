from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
]
