from django.urls import path,include
from . import views
app_name='store'

urlpatterns = [ 
    path('',views.index,name='index'),
    path('products',views.products, name='products'),
    path('intermOrder/<str:id>',views.intermOrder, name='intermOrder'),
    path('temp_cart/<str:id>',views.temp_cart, name='temp_cart'),
    
]
