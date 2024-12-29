"""
WSGI config for job project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job.settings')

# Set default port for Vercel
os.environ.setdefault('PORT', '8000')

application = get_wsgi_application()

# This is important for Vercel
app = application