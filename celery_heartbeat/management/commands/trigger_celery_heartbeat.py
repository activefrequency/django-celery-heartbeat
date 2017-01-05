from __future__ import unicode_literals, print_function, absolute_import, division

from django.core.management.base import BaseCommand
from celery_heartbeat.tasks import start_update_heartbeat


class Command(BaseCommand):

    def handle(self, *args, **options):
        start_update_heartbeat.delay()
