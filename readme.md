# 📚 AHBookStore – Django Bookstore Application

## Project Details
- Author: Harry Joseph ANd Abhishek Masur Jayatheertha
- Class: CPAN 214 Group Project Final
- Created: 2025-12-06
- Platform: Django Web Application
- Package Manager: pip
- Django Version: 5.2.8
- Database: SQLite3
- API Framework: Django REST Framework 3.16.1

## Overview
AHBookStore is a comprehensive Django web application that demonstrates full-stack web development with user authentication, CRUD operations, and REST API functionality. The project showcases modern Django practices including class-based views, user ownership validation, and browsable API interfaces.

**Important**: CRUD operations (Create, Update, Delete) are only available to registered users with accounts. Unregistered visitors can only browse books and view details.

super user = admin
password = admin123 to see the admin option you need to register and create an account

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)](https://www.djangoproject.com/)
[![REST Framework](https://img.shields.io/badge/DRF-3.16.1-red.svg)](https://www.django-rest-framework.org/)
[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit_App-success?style=for-the-badge)](https://ahbookstore.onrender.com/) 👈**
### **👉 Experience the full application functionality online app now: [https://ahbookstore.onrender.com/](https://ahbookstore.onrender.com/) 👈**
*✨ Fully deployed Django bookstore with user authentication, CRUD operations, and REST API*

---

## 📹 Testing Walkthrough
[VIEW COMPLETE TESTING WALKTHROUGH →](walkthrough.md)

We've created a comprehensive automated testing walkthrough that demonstrates all features of the AHBookStore application with video recordings and screenshots.

**All 20 test cases passed successfully!** View the [walkthrough.md](walkthrough.md) for detailed test results with embedded video demonstrations.
---


## Quick Download

**Get the complete project instantly:**

[![Download AHBookStoreFinalProject](https://img.shields.io/badge/Download-Project.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/AHBookStoreFinalProject/archive/refs/heads/main.zip)

*Complete Django project with bookstore functionality ready to run*
*Experience the full application functionality online*

## Important: Where your main code lives
- The core models are in [`books/models.py`](books/models.py) with Book model and user relationships
- The main views are in [`books/views.py`](books/views.py) with CRUD operations and authentication
- The REST API is in [`books/api/`](books/api/) with serializers and API endpoints

## Project Explorer
An interactive view of the Django application structure. All files are functional and documented.

<details open>
   <summary><strong>AHBookStore/ – Django Project Configuration</strong></summary>

   - 📁 <strong>AHBookStore</strong>
      - 📄 [`settings.py`](AHBookStore/settings.py) – Django settings with installed apps
      - 📄 [`urls.py`](AHBookStore/urls.py) – Root URL configuration
      - 📄 [`wsgi.py`](AHBookStore/wsgi.py) – WSGI deployment configuration
      - 📄 [`asgi.py`](AHBookStore/asgi.py) – ASGI deployment configuration
</details>

<details>
   <summary><strong>books/ – Main Application Logic</strong></summary>

   - 📁 <strong>books</strong>
      - 📱 [`models.py`](books/models.py) – **Book model with user relationships**
      - 🎯 [`views.py`](books/views.py) – **CRUD views with authentication**
      - 🔗 [`urls.py`](books/urls.py) – URL routing for book operations
      - 📝 [`forms.py`](books/forms.py) – Django forms for book input
      - 🔧 [`admin.py`](books/admin.py) – Django admin interface setup
      - 📁 <strong>api/</strong>
         - 🌐 [`views.py`](books/api/views.py) – **REST API endpoints**
         - 📊 [`serializers.py`](books/api/serializers.py) – **JSON serialization logic**
         - 🔗 [`urls.py`](books/api/urls.py) – API URL routing
      - 📁 <strong>templates/books/</strong>
         - 🏠 [`index.html`](books/templates/books/index.html) – Homepage template
         - 📖 [`detail.html`](books/templates/books/detail.html) – Book detail view
         - 📝 [`form.html`](books/templates/books/form.html) – Add/edit book form
         - 🗑️ [`confirm_delete.html`](books/templates/books/confirm_delete.html) – Delete confirmation
         - 🔐 [`auth_form.html`](books/templates/books/auth_form.html) – Login/registration
         - 🎨 [`layout.html`](books/templates/books/layout.html) – **Base template with navigation**
      - 📁 <strong>management/commands/</strong>
         - 🗃️ [`populate_books.py`](books/management/commands/populate_books.py) – **Sample data generator**
</details>

<details>
   <summary><strong>templates/ – Global Templates</strong></summary>

   - 📁 <strong>templates</strong>
      - 📁 <strong>rest_framework/</strong>
         - 🌐 [`api.html`](templates/rest_framework/api.html) – **Custom DRF template with branding**
</details>

<details>
   <summary><strong>Configuration & Dependencies</strong></summary>

   - 📦 [`requirements.txt`](requirements.txt) – Python dependencies
   - 🗃️ [`db.sqlite3`](.) – SQLite database file
   - 🔧 [`manage.py`](manage.py) – Django management script
   - 📝 [`README.md`](README.md) – Documentation (this file)
   - 🚫 [`.gitignore`](.gitignore) – Git exclusion rules
</details>

## File Structure

```text
AHBookStoreFinalProject/
├── 📁 AHBookStore/                  # Django project configuration
│   ├── ⚙️ settings.py               # Project settings & installed apps
│   ├── 🔗 urls.py                   # Root URL configuration
│   ├── 🚀 wsgi.py                   # WSGI deployment config
│   └── 🚀 asgi.py                   # ASGI deployment config
│
├── 📁 books/                        # Main books application
│   ├── 📱 models.py                 # Book model with user relationships
│   ├── 🎯 views.py                  # CRUD views with authentication
│   ├── 🔗 urls.py                   # URL routing for books
│   ├── 📝 forms.py                  # Django forms for input
│   ├── 🔧 admin.py                  # Admin interface setup
│   ├── 🧪 tests.py                  # Test placeholders
│   │
│   ├── 📁 api/                      # REST API functionality
│   │   ├── 🌐 views.py              # API endpoints (getBooks, getBook)
│   │   ├── 📊 serializers.py        # JSON serialization
│   │   └── 🔗 urls.py               # API URL routing
│   │
│   ├── 📁 templates/books/          # HTML templates
│   │   ├── 🏠 index.html            # Homepage with book list
│   │   ├── 📖 detail.html           # Individual book details
│   │   ├── 📝 form.html             # Add/edit book form
│   │   ├── 🗑️ confirm_delete.html   # Delete confirmation
│   │   ├── 🔐 auth_form.html        # Login/registration
│   │   └── 🎨 layout.html           # Base template with navigation
│   │
│   ├── 📁 static/                   # CSS styling
│   │   └── 🎨 style.css             # Application styles
│   │
│   ├── 📁 management/commands/      # Custom Django commands
│   │   └── 🗃️ populate_books.py     # Sample data generator
│   │
│   └── 📁 migrations/               # Database migrations
│       └── 🗃️ 0001_initial.py       # Initial model creation
│
├── 📁 templates/                    # Global templates
│   └── 📁 rest_framework/
│       └── 🌐 api.html              # Custom DRF interface
│
├── 📦 requirements.txt              # Python dependencies
├── 🗃️ db.sqlite3                   # SQLite database
├── 🔧 manage.py                     # Django management utility
├── 🚫 .gitignore                    # Git exclusions
└── 📝 README.md                     # Documentation
```





## Technology Stack

- **Backend**: Django 5.2.8
- **API**: Django REST Framework 3.16.1
- **Database**: SQLite3
- **Frontend**: Django Templates + CSS
- **Authentication**: Django Built-in Auth System

## Project Requirements Met

All 24 CPAN 214 Final Project requirements have been successfully implemented:

☑ Django project creation and configuration  
☑ Books app with proper routing  
☑ Template system with layout inheritance  
☑ Book model with all required fields  
☑ CRUD operations for books  
☑ User authentication system  
☑ Authorization and access control  
☑ Django REST Framework integration  
☑ API endpoints for external access  
☑ Comprehensive testing scenarios  

---



*This project demonstrates modern Django web development with REST API integration and proper authentication/authorization patterns.*
