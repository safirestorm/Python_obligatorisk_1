import requests
from dotenv import load_dotenv, set_key
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-key', action='store', help="Add your authentication")

args = parser.parse_args()

load_dotenv()
KEY = os.getenv('API_KEY')

if args.key is None and KEY is None:
    print('Tilføj API nøgle')
    exit()

if args.key is not None:
    set_key('.env', 'API_KEY', args.key)
    KEY = args.key

currency = str(input("Vælg Valuta "))

url = f'https://v6.exchangerate-api.com/v6/{KEY}/latest/{currency}'

# Laver sin request
response = requests.get(url)
data = response.json()

print(data)
