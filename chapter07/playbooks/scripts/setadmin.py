#!/usr/bin/env python3
""" A script to set the admin credentials """
# Assumes three environment variables
#
# PROJECT_DIR: root directory of the project
# PROJECT_APP: name of the project app
# ADMIN_PASSWORD: admin user's password
# ADMIN_EMAIL: admin user's email

import os
import sys

# Add the project directory to system path
proj_dir = os.path.expanduser(os.environ['PROJECT_DIR'])
sys.path.append(proj_dir)

proj_app = os.environ['PROJECT_APP']
os.environ['DJANGO_SETTINGS_MODULE'] = proj_app + '.settings'
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
u, _ = User.objects.get_or_create(username='admin')
u.is_staff = u.is_superuser = True
u.email = os.environ['ADMIN_EMAIL']
u.set_password(os.environ['ADMIN_PASSWORD'])
u.save()
