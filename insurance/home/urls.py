from django.urls import path
from home import views

urlpatterns = [
    path('', views.prediction, name='prediction'),
    path('about/', views.about, name='about'),
    
    
    
]