import requests
from datetime import datetime

QUOTE_FILE = 'quote.txt'
QUOTE_API_URL = 'https://zenquotes.io/api/random'


def get_quote():
    data = requests.get(QUOTE_API_URL)
    return data.json()[0]['q'], data.json()[0]['a']


def write_to_file(q, a):
    with open(QUOTE_FILE, 'a') as file:
        file.write(f"\n⏰ {datetime.now().strftime('%H:%M:%S')} 🌍 {q} 🌻 by {a} 💥")


quote, author = get_quote()
write_to_file(quote, author)
