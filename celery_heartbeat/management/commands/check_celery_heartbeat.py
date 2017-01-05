from __future__ import unicode_literals, print_function, absolute_import, division

from django.core.management.base import BaseCommand
from django.core.cache import cache
from django.conf import settings

from celery_heartbeat.utils import check_and_log_heartbeat


class Command(BaseCommand):

    def handle(self, *args, **options):
        check_and_log_heartbeat()
