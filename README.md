# Dynamic Vehicle Identification and Tracking System  

This project is a **Dynamic Vehicle Identification and Tracking System** designed to streamline the process of detecting and recognizing vehicle license plates. The system identifies the state associated with the vehicle's number plate when an image of the plate is uploaded.  

---

## 🚀 Features  

- **Home Page:**: Welcoming page with navigation options for easy access.
- **User Authentication:**: Secure registration and login functionality.
- **Image Upload**:Detects vehicle number plates and states from static images and .
- **Video Upload**: Perform dynamic number plate recognition from video files.
- **Results Pages:**: Displays extracted vehicle numbers and identified states.
-  **Contact Pages:**: Submit queries or feedback via a contact form.
-  **Responsive Design:**:  Styled with Bootstrap for compatibility across all devices.

---

## 🛠️ Technologies Used  

- **Frontend**: HTML, CSS, JavaScript, Bootstrap  
- **Backend**: Python, Django  
- **Machine Learning/AI**: Optical Character Recognition ( Pytesseract) for number plate detection  
- **Database**: SQLite (or any database of your choic)  

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
2. Upload an image and vedio of a vehicle's number plate.
3. View the state associated with the number plate.

## 💡 Key Functionality
1. Pytesseract OCR: Extracts number plate text from images and videos.
2. State Identification: Maps number plates to their respective states.
3. Image and Video Support: Handles both static and dynamic inputs.
4. Responsive Design: Ensures usability across devices using Bootstrap.

## 🧪 Testing

1. Test the application with sample images and videos of vehicle number plates.
2. Supported formats: .jpg, .png, .jpeg (for images) and .mp4, .avi (for videos).

## 📝 Notes

1. Pytesseract must be correctly installed and configured for the OCR functionality to work.
2. The application uses SQLite (db.sqlite3) as the default database.
## 🤝 Acknowledgements
1. Pytesseract: OCR tool used for number plate recognition.
2. Django Framework: Backend framework powering the application.
3. Bootstrap: Frontend framework for responsive styling.
## 👩‍💻 Author
### Dhinakaran R
#### -**Email:** dhinadhina417@gmail.com
-**GitHub:** https://github.com/Dhina0504
