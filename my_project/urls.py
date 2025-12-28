from django.urls import path, include
from accounts import views



urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),  
    
]
