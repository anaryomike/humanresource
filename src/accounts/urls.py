from django.urls import path
from .import views


app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('create-user/',views.register_user_view,name='register'),
    path('user/change-password/',views.changepassword,name='changepassword'),
    path('user/profile/view/',views.user_profile_view,name='userprofile'),
   

    #Users Views
    path('users/all',views.users_list,name='users'),
    path('users/<int:id>/block',views.users_block,name='userblock'),
    path('users/<int:id>/unblock',views.users_unblock,name='userunblock'),
    path('users/blocked/all',views.users_blocked_list,name='erasedusers'),


]

