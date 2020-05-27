from django.urls import path, re_path
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    re_path(r'^register',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

]
