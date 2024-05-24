from mailings.utils import test_print_time
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        test_print_time()
