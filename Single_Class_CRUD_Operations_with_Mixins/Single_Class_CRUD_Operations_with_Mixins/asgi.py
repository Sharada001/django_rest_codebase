"""
ASGI config for Single_Class_CRUD_Operations_with_Mixins project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Single_Class_CRUD_Operations_with_Mixins.settings')

application = get_asgi_application()
