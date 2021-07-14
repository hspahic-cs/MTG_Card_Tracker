from csv import DictReader

from django.core.management import BaseCommand

from cards.models import Card
from pytz import UTC

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from cardCollection.csv into our Card mode"

    def handle(self, *args, **options):
        if Card.objects.exists():
            print('Card data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Loading card data for cards in card_collection")
        for row in DictReader(open('./card_collection.csv')):
            card = Card()
            card.name = row['Name']
            card.quantity = row['Quantity']
            card.cardSet = row['Set']
            card.cost = row['Cost']
            card.save()
