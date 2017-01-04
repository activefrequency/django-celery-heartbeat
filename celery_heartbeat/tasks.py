from __future__ import unicode_literals, print_function, absolute_import, division

from django.core.cache import cache
from celery import shared_task

import time

from celery_heartbeat.utils import get_cache_key


@shared_task(ignore_result=True, name='celery_heartbeat.shared_task')
def update_heartbeat():
    cache_key = get_cache_key()
    cache.set(cache_key, long(time.time()), None)
