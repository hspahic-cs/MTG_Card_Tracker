from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


'''
Updates the price for every card in collection
'''
def updateCollection(filepath):
    cardCollection = []
    fields = []

    # Take csv file and convert to readable format

    with open(filepath, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        # Name, Quantity, Set, Cost, Img
        print(fields)

        for i, row in enumerate(csvreader):
            print(row)
            setWords = row[2].split()
            nameWords = row[0].split()
            setWords = "+".join(setWords)
            nameWords = "+".join(nameWords)

            # Goes to Url
            url = f"https://www.mtggoldfish.com/price/{setWords}/{nameWords}#paper"
            page = urlopen(url)

            # Scrapes price
            soup = BeautifulSoup(page, "html.parser")
            price = soup.find('div',{'class': 'price-box-price'}).text
            img = soup.find('img', {'class': 'price-card-image-image'})['src']
            price = price[2:]

            # Updates price & adds to collection holder
            row[3] = price
            row[4] = img;
            cardCollection.append(row)

        csvfile.close()

    # Opens csv into 'Write' mode
    with open(filepath, "w", newline = '') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(cardCollection)

if __name__ == "__main__":
    updateCollection("card_collection.csv")
