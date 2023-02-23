from django.core.management import BaseCommand, CommandError

from nplusone.management.commands import _provider


class Command(BaseCommand):
    help = 'Setting dump datas'

    def add_arguments(self, parser):
        parser.add_argument('cnt', nargs=1, type=int)

    def handle(self, *args, **options):
        try:
            cnt = int(options['cnt'][0])
        except ValueError:
            raise CommandError('Not integer.')

        if cnt <= 0:
            raise CommandError('Greater than or equal to 1.')

        for i in range(cnt):
            _provider.WebToonFactory()
