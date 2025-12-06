# 📚 AHBookStore – Django Bookstore Application

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)](https://www.djangoproject.com/)
[![REST Framework](https://img.shields.io/badge/DRF-3.16.1-red.svg)](https://www.django-rest-framework.org/)
[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Visit_App-success?style=for-the-badge)](https://ahbookstore.onrender.com/)

## 🌟 **LIVE DEMO**
### **👉 Experience the app now: [https://ahbookstore.onrender.com/](https://ahbookstore.onrender.com/) 👈**

*✨ Fully deployed Django bookstore with user authentication, CRUD operations, and REST API*

---

## Project Metadata
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

## Quick Download

**Get the complete project instantly:**

[![Download AHBookStoreFinalProject](https://img.shields.io/badge/Download-Project.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/AHBookStoreFinalProject/archive/refs/heads/main.zip)

*Complete Django project with bookstore functionality ready to run*

## Live Demo

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://ahbookstore.vercel.app)

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


## Features Implemented

### Core Requirements ✅
- **Django Project Setup** - Complete bookstore application
- **Book Model** - Title, author, year, rating, description with user ownership
- **Browse Functionality** - All users can view books and details (no account required)
- **CRUD Operations** - Create, Update, Delete (requires user registration and login)
- **User Authentication** - Registration, login, logout with validation
- **Authorization** - Ownership-based edit/delete restrictions
- **Template System** - Base layout with navigation and responsive design
- **Admin Interface** - Django admin for book management

### REST API ✅
- **Django REST Framework** - Browsable API interface
- **API Endpoints**:
  - `GET /api/books/` - Retrieve all books
  - `GET /api/books/<id>/` - Retrieve specific book
- **JSON Serialization** - Clean API responses
- **Custom DRF Templates** - Branded API interface

### Advanced Features ✅
- **User Ownership Validation** - Users can only edit their own books
- **Access Control** - Book creation requires user registration and login
- **Browse Mode** - Unregistered users can view all books but cannot modify them
- **Admin Access Control** - Admin panel option only visible to authenticated users in navigation
- **Error Handling** - Comprehensive form validation and error messages
- **Sample Data Management** - Custom command to populate test data
- **Responsive Navigation** - Conditional menu items based on authentication status
- **Security** - Login required decorators and permission checks


## Technology Stack

- **Backend**: Django 5.2.8
- **API**: Django REST Framework 3.16.1
- **Database**: SQLite3
- **Frontend**: Django Templates + CSS
- **Authentication**: Django Built-in Auth System

## Project Requirements Met

All 24 CPAN 214 Final Project requirements have been successfully implemented:

✅ Django project creation and configuration  
✅ Books app with proper routing  
✅ Template system with layout inheritance  
✅ Book model with all required fields  
✅ CRUD operations for books  
✅ User authentication system  
✅ Authorization and access control  
✅ Django REST Framework integration  
✅ API endpoints for external access  
✅ Comprehensive testing scenarios  

---

*This project demonstrates modern Django web development with REST API integration and proper authentication/authorization patterns.*
