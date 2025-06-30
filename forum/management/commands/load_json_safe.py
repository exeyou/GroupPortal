from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Loads data from data.json using utf-8 safe method'

    def handle(self, *args, **kwargs):
        call_command('loaddata', 'data.json')
