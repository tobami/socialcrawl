from django.core.management.base import BaseCommand, CommandError
from socialcrawl.clients.crawler import CachedTwitterClient


class Command(BaseCommand):
    help = 'runs your code in the django environment'

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('You need to specify a username')
        client = CachedTwitterClient()
        self.stdout.write(str(client.get_profile(args[0])))
