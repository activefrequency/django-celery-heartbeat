from __future__ import unicode_literals, print_function, absolute_import, division

from django.conf import settings
from django.core.cache import cache
from celery import Celery

import time
import logging


logger = logging.getLogger('celery_heartbeat')
DEFAULT_CELERY_HEARTBEAT_DELAY_THRESHOLD = 5 * 60


def get_cache_key(queue_name):
    '''Returns the name of the cache key to use for the given queue.'''

    prefix = getattr(settings, 'CELERY_HEARTBEAT_CACHE_KEY', 'CELERY_HEARTBEAT_CACHE_KEY')
    prefix = prefix or 'CELERY_HEARTBEAT_CACHE_KEY'

    return '{}-{}'.format(prefix, queue_name)


def get_known_queues():
    '''Returns a list of monitored celery queues.'''

    app = Celery()
    app.config_from_object('django.conf:settings')

    queues = list(set(getattr(settings, 'CELERY_HEARTBEAT_MONITORED_QUEUES', []) or []))
    if not queues:
        queues = list(app.amqp.queues.keys())

    return queues


def check_heartbeat(threshold):
    '''Checks if any of the queues have fallen behind by more than threshold
    seconds and returns human-readable status.'''

    errors = []

    for queue in get_known_queues():

        cache_key = get_cache_key(queue)
        heartbeat = cache.get(cache_key)
        if not heartbeat:
            continue

        delta = long(time.time() - heartbeat)

        if delta > threshold:
            errors.append('Celery queue "{}" has fallen behind by {} seconds.'.format(queue, delta))

    return errors


def check_and_log_heartbeat():
    '''Checks if any of the queues have fallen behind by more than threshold
    seconds and logs any queues that did.'''

    errors = check_heartbeat(get_threshold())
    if errors:
        logger.error('\n'.join(errors))


def get_threshold():
    '''Returns the configured or default threshold for queues falling behind, in seconds.'''

    threshold = getattr(settings, 'CELERY_HEARTBEAT_DELAY_THRESHOLD', DEFAULT_CELERY_HEARTBEAT_DELAY_THRESHOLD)
    return threshold or DEFAULT_CELERY_HEARTBEAT_DELAY_THRESHOLD
