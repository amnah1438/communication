from pathlib import Path
import os
import cloudinary

# =========================
# 📁 Base Directory
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================
# 🔐 Security
# =========================
SECRET_KEY = 'django-insecure-mih^n7urj&0w-!nflo_q76jk3@k!opmgbrgdjo5*-!q@wt^@-g'
DEBUG = True
ALLOWED_HOSTS = ['*']

# =========================
# 📦 Applications
# =========================
INSTALLED_APPS = [
    # Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # Django default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
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
    cloud_name=os.getenv("dyg4401o9"),
    api_key=os.getenv("283452178212273"),
    api_secret=os.getenv("hRYpVPeOwKcCDSruJ9Um_56WdVwT"),
    secure=True
)

# تخزين الميديا على Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# =========================
# 🆔 Default PK
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'