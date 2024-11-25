# Dynamic Vehicle Identification and Tracking System  

This project is a **Dynamic Vehicle Identification and Tracking System** designed to streamline the process of detecting and recognizing vehicle license plates. The system identifies the state associated with the vehicle's number plate when an image of the plate is uploaded.  

---

## 🚀 Features  

- **Number Plate Recognition**: Automatically detects and extracts details from the uploaded number plate image.  
- **State Identification**: Displays the state corresponding to the number plate.  
- **User-Friendly Interface**: Simplified upload functionality for easy interaction.  

---

## 🛠️ Technologies Used  

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Python, Django  
- **Machine Learning/AI**: Optical Character Recognition (OCR) for number plate detection  
- **Database**: SQLite (or any database of your choice)  

---

## 📂 Project Structure  

vehiclerecognition/  
├── detection/                    # Main application  
│   ├── __pycache__/              # Compiled Python files  
│   ├── images/                   # Image files for processing  
│   ├── migrations/               # Django database migrations  
│   ├── static/                   # Static files (CSS, JS, etc.)  
│   ├── templates/                # HTML templates  
│   │   ├── contact.html          # Contact page  
│   │   ├── dashboard.html        # Dashboard page  
│   │   ├── index.html            # Homepage  
│   │   ├── login.html            # Login page  
│   │   ├── register.html         # Registration page  
│   │   ├── result.html           # Display results  
│   │   ├── services.html         # Services page  
│   │   ├── upload_image.html     # Image upload page  
│   │   └── base.html             # Base HTML template  
│   ├── admin.py                  # Django admin configurations  
│   ├── apps.py                   # App configurations  
│   ├── forms.py                  # Forms for user input  
│   ├── models.py                 # Database models  
│   ├── svm_model.pkl             # Pre-trained SVM model for OCR  
│   ├── tests.py                  # Test cases  
│   ├── urls.py                   # URL routing  
│   ├── utils.py                  # Utility functions  
│   └── views.py                  # Application logic and endpoints  
├── media/                        # Folder for uploaded files  
├── vehiclerecognition/           # Project-level configurations  
│   ├── __init__.py               # Package initialization  
│   ├── asgi.py                   # ASGI configuration  
│   ├── settings.py               # Django project settings  
│   ├── urls.py                   # Project-wide URL configuration  
│   └── wsgi.py                   # WSGI configuration  
├── manage.py                     # Django project management script  
└── README.md                     # Project documentation  

## ⚙️ Installation  

Follow these steps to set up the project locally:  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/your-username/dynamic-vehicle-identification.git  
   cd dynamic-vehicle-identification  

2. **Set up Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  


3. **Install Dependencies:**:
    ```bash
    pip install -r requirements.txt  

5. **Run Migrations:**:
   ```bash
   python manage.py migrate  

6.  **Start the Server:**:
    ```bash
    python manage.py runserver
## 🖼️ Usage
1. Log in or register to access the system.
2. Upload an image of a vehicle's number plate.
3. View the state associated with the number plate.
