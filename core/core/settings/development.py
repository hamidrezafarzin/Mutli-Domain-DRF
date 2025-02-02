from .base import *
import socket

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

CORS_ALLOW_ALL_ORIGINS = True

SHOW_DEBUGGER_TOOLBAR = True

CSRF_TRUSTED_ORIGINS = [
    "https://*.127.0.0.1",
    "https://localhost",
]

REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
    "anon": "1000/minute",  # Higher rate limit for testing
    "user": "1000/minute",
}

USE_S3 = config("USE_S3", cast=bool, default=True)

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
