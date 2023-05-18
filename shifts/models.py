from django.db import models
import datetime
from typing import Optional
import warnings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser