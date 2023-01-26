from django.urls import path,include
from rest_framework import routers
from .import views


# router = routers.DefaultRouter(trailing_slash=False)


router = routers.DefaultRouter()

router.register('booking', views.SingleMenuItemView, basename='menu')


urlpatterns = [
     path('', views.home, name="home"),
     path("register/", views.register_request, name="register"),
     path("login/", views.login_request, name="login"),
     path("logout/", views.logout_request, name= "logout"),
     path('booking/', views.BookingViewSet.as_view(), name="booking"),
     path('booking/<int:pk>', views.SingleBookingViewSet.as_view(), name="booking_item"),
     path('menu-items/', views.MenuItemView.as_view(), name="menu"),
     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), ),

     
 ]
 