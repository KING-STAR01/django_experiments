from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "simple management command for testing"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the person to greet')

    def handle(self, *args, **options):
        print("hello", options['name'])

        self.stdout.write(
                self.style.SUCCESS("Successfully greeted {}".format(options['name']))
                )
