from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

ALLOWED_HOSTS = ["api.example.com", "127.0.0.1"]

SHOW_DEBUGGER_TOOLBAR = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://api.example.com",
    "https://api.example.com",

]

CSRF_TRUSTED_ORIGINS = [
    "https://*.127.0.0.1",
    "https://api.example.com",
]

REST_FRAMEWORK.update(
    {"DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",)}
)


# security Configs :

# X-content-type-option
SECURE_CONTENT_TYPE_NOSNIFF = True

# X-Frame-Options
X_FRAME_OPTIONS = "DENY"
USE_X_FORWARDED_HOST = True

# hsts
SECURE_HSTS_SECONDS = 10368000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# session cookie Security for xss
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = False  # True
SESSION_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_NAME = "prefix_sessionid"

# session cookie Security for csrf
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False  # True
CSRF_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_NAME = "prefix_csrftoken"

# ssl redirection
SECURE_SSL_REDIRECT = False  # True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# xss protection
SECURE_BROWSER_XSS_FILTER = True

# REFERRER POLICY
SECURE_REFERRER_POLICY = "strict-origin"
