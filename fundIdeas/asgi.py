# import necessary libraries
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fundIdeas.settings')
application = get_asgi_application()
