from django.urls import path
from . import views
app_name='c_app'

urlpatterns = [ 
    path('',views.UserLogin,name='login'),
    path('register',views.UserRegisteration,name='register'),
    path('change',views.change,name='change'),
    path('logout',views.logout,name='logout'),
    # path('activate/<str:uidb64>/<str:token>',views.activate,name='activate'),
    
]
