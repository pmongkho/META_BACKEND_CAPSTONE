from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .forms import BookingForm
import json
from rest_framework.response import Response


# Create your views here.

def home(request):
    return render(request, 'index.html')

class MenuItemView(generics.ListCreateAPIView,APIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    template_name = 'menu.html'
    
    def get(self, request):
        content = Menu.objects.all()
        return render(request, self.template_name, {'content':content})
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    
class BookingViewSet(APIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]
    template_name = "booking.html"
    
    def get(self, request):
        content = Booking.objects.all()
        return render(request, self.template_name, {'content':content})
    def post(self, request, *args, **kwargs):  
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)   
    
class SingleBookingViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    
    
    

