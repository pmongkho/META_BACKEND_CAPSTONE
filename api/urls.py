from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
     path('restaurant/booking/', include(router.urls)),
     path('menu-items/', views.MenuItemView.as_view()),
     path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
 ]
 