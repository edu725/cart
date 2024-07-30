from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login1/', login_dashbord, name='login1'),
    path('register1/', register_dashbord, name='register1'),
    path('logout1/', logout_dashbord, name='logout1'),
]