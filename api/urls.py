from django.urls import path,include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'tables', views.BookingViewSet)

urlpatterns = [
     path('home/', views.home, name="home"),
     path('booking/', views.BookingViewSet.as_view(), name="booking"),
     path('booking/<int:pk>', views.SingleBookingViewSet.as_view()),
     path('menu-items/', views.MenuItemView.as_view(), name="menu"),
     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
     
 ]
 