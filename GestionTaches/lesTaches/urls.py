from django.urls import path, include 
from . import views 
from rest_framework.routers import DefaultRouter 
from .views import TaskViewSet 
 
# Create a router instance and register your viewset 
router = DefaultRouter() 
router.register(r'lesTaches', TaskViewSet) 
 
urlpatterns=[ 
path('home',views.home,name='home'), 
path('listing', views.task_listing,name="listing"), 
path('', include(router.urls)), 
] 