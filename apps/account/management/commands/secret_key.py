from colorama import Fore, Style
from django.core.management import utils
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("*" * 10 + "< Your django secret key >" + "*" * 10 + "\n")
        print("\t" + utils.get_random_secret_key() + "\n")
        print("*" * 10 + "< Your django secret key >" + "*" * 10)
