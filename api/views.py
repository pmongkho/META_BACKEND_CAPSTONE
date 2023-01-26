from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import *
from .serializers import *
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate, logout #add this
from rest_framework.response import Response
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration.html", context={"register_form":form})
        
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


class MenuItemView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, AllowAny]
    template_name = 'menu.html'
    
    def get(self, request):
        content = Menu.objects.all()
        return render(request, self.template_name, {'content':content})
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView,generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]
    template_name = "menu__item.html"
    
    def get(self, request, **kwargs):
        content = Menu.objects.get(pk=self.kwargs.get('pk'))
        return render(request, self.template_name, {'content':content})

    
class BookingViewSet(APIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    template_name = "booking.html"
    
    def get(self, request):
        content = Booking.objects.all()
        return render(request, self.template_name, {'content':content})
    def post(self, request, *args, **kwargs):  
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return render(request, self.template_name)   
    
class SingleBookingViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    template_name = "booking__item.html"
    
    # def get(self, request, **kwargs):
    #     content = Booking.objects.get(pk=self.kwargs.get('pk'))
    #     return render(request, self.template_name, {'content':content})
    
    

    
    

