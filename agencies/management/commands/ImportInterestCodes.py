import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from agencies.models import StaffingAgency
from temps.models import InterestCode


class Command(BaseCommand):
    def handle(self, *args, **options):
        csv_file_path = '%s/storage/temp/soc_2010_alphabetical_index.csv' % settings.BASE_DIR

        agency = StaffingAgency.objects.get(name='Tempsurge')

        with open(csv_file_path, 'rb') as csvfile:
            temp_reader = csv.DictReader(csvfile)

            i = 0

            for row in temp_reader:
                i += 1

                print row

                # Create temp profile
                t = InterestCode.objects.create(
                    name=row['name'],
                    code=row['code'],
                    agency=agency,
                )

                self.stdout.write('------------------------------')