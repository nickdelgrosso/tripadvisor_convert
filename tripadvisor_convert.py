import json
from bs4 import BeautifulSoup
import pandas as pd
from os import path


def parse_json(filename):
    """Return a Pandas DataFrame with Reviews from the JSON File given."""

    with open(filename) as f:
        data = json.load(f)
        reviews = data['Reviews']
        info = data['HotelInfo']

    df = pd.DataFrame()
    for review in reviews:
        rr = pd.Series(review['Ratings'], name=review['ReviewID'])
        rr['Date'] = review['Date']
        rr['Author'] = review['Author']
        rr['AuthorLocation'] = review['AuthorLocation'].split(', ')[-1]
        df = df.append(rr)


    # Hotel Info
    df['HotelID'] = int(info['HotelID'])
    df['Hotel'] = info['Name']
    price_range = [int(''.join([el for el in price if el.isdigit()])) for price in info['Price'].split('-')]
    df['PriceMin'] = price_range[0]
    df['PriceMax'] = price_range[-1]
    address = BeautifulSoup(info['Address'], 'lxml')
    region = address.find('span', property='v:region').text
    df['HotelLocation'] = region

    return df


def to_csv(json_filename, csv_filename):
    if not csv_filename:
        csv_filename = path.basename(json_filename) + '.csv'
    df.to_csv(csv_filename)


if __name__ == '__main__':
    filename = '73739.json'
    df = parse_json(filename)

    print(df.head(2))