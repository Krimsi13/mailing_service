from mailings.utils import send_mailing
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(send_mailing())
