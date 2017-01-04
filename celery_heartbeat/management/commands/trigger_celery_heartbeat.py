from __future__ import unicode_literals, print_function, absolute_import, division

from django.core.management.base import BaseCommand
from celery_heartbeat.tasks import update_heartbeat


class Command(BaseCommand):

    def handle(self, *args, **options):
        update_heartbeat.delay()
