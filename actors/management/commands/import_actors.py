from django.core.management.base import BaseCommand
import csv
from datetime import datetime
from actors.models import Actor

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo contendo os atores a serem importados'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='cp1252') as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                name = row['name']
                birthday = datetime.strptime(
                    row['birthday'],
                    '%d/%m/%Y'
                ).date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(f'Importando ator: {name}'))

                Actor.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )

        self.stdout.write(self.style.SUCCESS('Atores importados com sucesso!'))
