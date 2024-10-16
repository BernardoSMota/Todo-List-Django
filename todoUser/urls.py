from django.urls import path
from todoUser.views import createUser, loginUser, logoutUser

app_name='todoUser'

urlpatterns = [
    path('user/create/', createUser, name='create'),
    path('user/login/', loginUser , name='login'),
    path('user/logout/', logoutUser , name='logout'),
]
