import os
import sys
from pathlib import Path

# Add the project to the Python path
sys.path.append(str(Path(__file__).parent))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AHBookStore.settings')

import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Configure Django
django.setup()

# Create the WSGI application
application = get_wsgi_application()

# For Vercel, we need to handle this as a handler function
def handler(request):
    return application(request)