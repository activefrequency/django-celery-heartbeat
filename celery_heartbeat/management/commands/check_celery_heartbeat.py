from __future__ import unicode_literals, print_function, absolute_import, division

from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.conf import settings

from celery_heartbeat.utils import get_cache_key

import time
import logging

logger = logging.getLogger('celery_heartbeat')


class Command(BaseCommand):
    DEFAULT_CELERY_HEARTBEAT_DELAY_THRESHOLD = 5# * 60

    def handle(self, *args, **options):
        cache_key = get_cache_key()
        heartbeat = cache.get(cache_key)
        if not heartbeat:
            print('hello')
            return

        delta = long(time.time() - heartbeat)
        threshold = getattr(settings, 'CELERY_HEARTBEAT_DELAY_THRESHOLD', self.DEFAULT_CELERY_HEARTBEAT_DELAY_THRESHOLD) or self.DEFAULT_CELERY_HEARTBEAT_DELAY_THRESHOLD

        if delta > threshold:
            logger.error('Celery is behind by {} seconds.'.format(delta))

