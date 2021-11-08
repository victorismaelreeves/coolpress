from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Get the latest news from mediastack'

    def add_arguments(self, parser):
        parser.add_argument(
            '--countries',
            nargs='+',
            efault=['us'],
            help='Countries'
        )
        parser.add_argument(
            '--limit',
            action='store',
            help='Change the default 10 news per execution',
            default=10,
            type=int
        )

    def handle(self, *args, **options):
        countries = options['countries']
        limit = options['limit']
        single_countries = []
    
        for country in countries:
            if ',' in country:
                single_countries.extend(country.split(','))
            else:
                single_countries.append(country)

        inserted_posts = gather_and_create_news(['en'], limit, single_countries)

        self.stdout.write(
            f'Inserted {len(inserted_posts)} posts from {single_countries} with limit: {limit}')