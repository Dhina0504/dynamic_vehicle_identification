from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from PIL import Image
from .models import *
import numpy as np
import pytesseract
import os




# Replace 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' with the actual installation path on your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load mappings of state and district codes (this should be a dictionary or function you define)
state_district_map = {
    "KA": "Karnataka",
    "MH": "Maharashtra",
    "DL": "Delhi",
    "TN":"TamilNadu",
    "MP":"Madhyapradesh",
    "MN":"Manipur",
    "OD":"Odisha",
    "WB":"WestBengal",
    # Add other mappings as needed
}

# Function to extract state and district from the vehicle number
def extract_state_and_district(plate_text):
    # Extract the first two characters to identify the state
    state_code = plate_text[:2].upper()
    state = state_district_map.get(state_code, "Unknown State")
    # Add custom logic here if you want to extract district codes or other details from the plate text
    return state

# Home view
def home_view(request):
    return render(request, 'detection/index.html')
def services_view(request):
    return render(request, 'detection/services.html')

def contact_view(request):
    return render(request, 'detection/contact.html')
# def Homepage(request):
#     return render(request,'index.html')

# Register view

def login_register_view(request):
    if request.method == 'POST':
        if request.POST.get('type') == "Register":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect('upload_image')

        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('upload_image')
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, 'detection/login.html')


'''def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('upload_image')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'detection/login.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('upload_image')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login details.")
    else:
        form = AuthenticationForm()
    return render(request, 'detection/login.html', {'form': form})
'''
# Logout view
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')



# Upload Image view for vehicle number plate detection
@login_required(login_url='login')
def upload_image_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            uploaded_image = UploadedImage(user=request.user, image=image)
            uploaded_image.save()

            try:
                img = Image.open(uploaded_image.image.path)

                # Use pytesseract to extract text from the image
                plate_text = pytesseract.image_to_string(img, config='--psm 8')
                plate_text = plate_text.replace("\n", "").strip()  # Clean up the text

                if plate_text:
                    # Extract state from the detected text
                    state = extract_state_and_district(plate_text)  # Modify this function to return only the state
                    result = f"Detected Vehicle Number: {plate_text}, State: {state}"
                    uploaded_image.plate_text = plate_text
                    uploaded_image.state = state
                else:
                    result = "No text detected. Please try again with a clearer image."
                    uploaded_image.plate_text = "No text detected"
                    uploaded_image.state = ""

                uploaded_image.save()

                # Return the result or render a template with the result
                return render(request, 'detection/result.html', {'prediction': result})

            except Exception as e:
                messages.error(request, f"An error occurred while processing the image: {str(e)}")
                return redirect('upload_image')
        else:
            messages.error(request, "Please upload a valid image.")

    else:
        form = ImageUploadForm()

    return render(request, 'detection/upload_image.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    uploaded_images = UploadedImage.objects.filter(user=request.user)
    errors = {}

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'profile':
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            height = request.POST.get('height')
            weight = request.POST.get('weight')

            if not gender:
                errors['gender'] = 'Gender is required.'
            if not age or int(age) < 0 or int(age) > 120:
                errors['age'] = 'Please enter a valid age.'
            if not height or int(height) <= 0 or int(height) > 300:
                errors['height'] = 'Please enter a valid height in cm.'
            if not weight or int(weight) <= 0 or int(weight) > 500:
                errors['weight'] = 'Please enter a valid weight in kg.'

            if not errors:
                user_profile.gender = gender
                user_profile.age = age
                user_profile.height = height
                user_profile.weight = weight
                user_profile.save()
                return redirect('dashboard')

        elif form_type == 'upload_image':
            image = request.FILES.get('image')
            if image:
                uploaded_image = UploadedImage(user=request.user, image=image)
                uploaded_image.save()
                return redirect('dashboard')

    return render(request, 'detection/dashboard.html', {
        'user_profile': user_profile,
        'uploaded_images': uploaded_images,
        'errors': errors
    })

