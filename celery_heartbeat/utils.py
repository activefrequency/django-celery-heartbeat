
from django.conf import settings


def get_cache_key():
    return getattr(settings, 'CELERY_HEARTBEAT_CACHE_KEY', 'CELERY_HEARTBEAT_CACHE_KEY') or 'CELERY_HEARTBEAT_CACHE_KEY'
