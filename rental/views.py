from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Car,  ContactDetail, Role, User
from django.utils import timezone
from datetime import datetime

def home(request):
    
    if request.user.is_authenticated:
        
        cars = Car.objects.filter(available=True).order_by('?')[:3]  
        return render(request, 'home.html', {'cars': cars})
    else:
        
        return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cars(request):
    cars = Car.objects.filter(available=True)
    return render(request, 'cars.html', {'cars': cars})

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            
            ContactDetail.objects.create(
                email=email,
                phone=request.POST.get('phone', ''),  
                message=f"From: {name}\nSubject: {subject}\nMessage: {message}"
            )
            
            messages.success(request, 'Message sent successfully!')
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return render(request, 'contact.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            
            user = User.objects.get(email=email)
            
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Invalid email or password.'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid email or password.'})
    
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            phone = request.POST.get('phone')
            role_name = request.POST.get('role')
            
            
            if password != confirm_password:
                return JsonResponse({'success': False, 'error': 'Passwords do not match.'})
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'error': 'Username already exists.'})
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'error': 'Email already exists.'})
            
            
            role, created = Role.objects.get_or_create(role_name=role_name)
            
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,  
                phone=phone,
                role=role
            )
            
            
            if role_name == 'admin':
                user.is_staff = True
                user.is_superuser = True
                user.save()
            
            
            login(request, user)
            return JsonResponse({'success': True})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return render(request, 'signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_car(request):
    if not request.user.is_staff:
        return JsonResponse({'success': False, 'error': 'Unauthorized access'})
    
    if request.method == 'POST':
        try:
            
            make = request.POST.get('name')
            model = request.POST.get('transmission')  
            car_type = request.POST.get('transmission')
            year = int(request.POST.get('year'))
            daily_rate = float(request.POST.get('price'))
            image_url = request.POST.get('image_url')
            
            
            car = Car.objects.create(
                make=make,
                model=model,
                car_type=car_type,
                year=year,
                daily_rate=daily_rate,
                image_url=image_url,
                created_by=request.user
            )
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
