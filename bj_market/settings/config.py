from decouple import config, Csv


SECRET_KEY = config('SECRET_KEY')
# Список доменов, которые может обслуживать Django (если DEBUG=False)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
DEBUG = config('DEBUG', default=True, cast=bool)

PAYPAL_MODE = config('PAYPAL_MODE')
PAYPAL_CLIENT_ID = config('PAYPAL_CLIENT_ID')
PAYPAL_CLIENT_SECRET = config('PAYPAL_CLIENT_SECRET')
