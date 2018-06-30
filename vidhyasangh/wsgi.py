"""
WSGI config for vidhyasangh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
# import sys

from django.core.wsgi import get_wsgi_application

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
# path = '/home/Gassymule/Skeletonv3.1/skeletonv3'
# if path not in sys.path:
#    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vidhyasangh.settings")

application = get_wsgi_application()
