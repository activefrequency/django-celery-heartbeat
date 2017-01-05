from __future__ import unicode_literals, print_function, absolute_import, division

from django.core.cache import cache
from celery import shared_task

import time

from celery_heartbeat.utils import get_cache_key, get_known_queues


@shared_task(ignore_result=True, name='celery_heartbeat.update_heartbeat')
def update_heartbeat(queue_name):
    '''Updates the given queue heartbeat value in the cache with the current timestamp.'''

    cache_key = get_cache_key(queue_name)
    cache.set(cache_key, long(time.time()), None)


@shared_task(ignore_result=True, name='celery_heartbeat.start_update_heartbeat')
def start_update_heartbeat():
    '''Schedules all heartbeat updates for all the queues.'''

    for queue in get_known_queues():
        update_heartbeat.apply_async(args=[queue], queue=queue)
