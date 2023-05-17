from dotenv import load_dotenv
import os
import requests

load_dotenv()
NYTBestSellersUrlAndApiKey = os.getenv("BOOKS_API_FULL_URL")

# API URL
# https://api.nytimes.com/svc/books/v3/lists/best-sellers
r = requests.get(NYTBestSellersUrlAndApiKey)
bestSellersList = r.json()['results']['books']

for book in bestSellersList:
    print(book['title'], 'by', book['author'])
