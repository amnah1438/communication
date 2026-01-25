from pathlib import Path
import os
from dotenv import load_dotenv
import cloudinary

# =========================
# 📁 Base Directory
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# 🔐 Load .env
# =========================
load_dotenv(os.path.join(BASE_DIR, '.env'), override=True)

# =========================
# 🔐 Security
# =========================
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-mih^n7urj&0w-!nflo_q76jk3@k!opmgbrgdjo5*-!q@wt^@-g'
)

DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']

DJANGO_ENV = os.getenv('DJANGO_ENV', 'development')

# =========================
# ☁️ Cloudinary ENV
# =========================
os.environ["CLOUDINARY_CLOUD_NAME"] = os.getenv("CLOUDINARY_CLOUD_NAME")
os.environ["CLOUDINARY_API_KEY"] = os.getenv("CLOUDINARY_API_KEY")
os.environ["CLOUDINARY_API_SECRET"] = os.getenv("CLOUDINARY_API_SECRET")

# =========================
# 📦 Applications
# =========================
INSTALLED_APPS = [
    'cloudinary',
    'cloudinary_storage',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]

# =========================
# 🧱 Middleware
# =========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =========================
# 🌐 URLs & Templates
# =========================
ROOT_URLCONF = 'communication.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'communication.wsgi.application'

# =========================
# 🗄️ Database
# =========================
if DJANGO_ENV == 'production':
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DB_ENGINE'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'CONN_MAX_AGE': 600,
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# =========================
# 🔑 Password Validators
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================
# 🌍 Localization
# =========================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# =========================
# 🎨 Static Files
# =========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# =========================
# ☁️ Cloudinary Configuration
# =========================
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# =========================
# 🆔 Default PK
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
