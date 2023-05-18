from dotenv import load_dotenv
import os
import requests


load_dotenv()
NYT_bestsellers_fiction_API = os.getenv("BOOKS_API_FICTION")
NYT_bestsellers_nonfiction_API = os.getenv("BOOKS_API_NONFICTION")


def call_api_and_get_json_data(API_URL):
    """ 
    Calls the NYT Best Seller API and returns the raw JSON data.
    - Expects a valid api URL with api key included
    - Returns json data format
    """

    r = requests.get(API_URL)
    return r.json()

def create_book_list(API_URL):
    """
    Takes NYT best seller data as json data, grabs the relevant info, and creates a new list of stripped down data to return.
    - Expects a balid api URL with api key included.
    - Returns a list of dictionaries.
    """
    
    data = call_api_and_get_json_data(API_URL)
    the_list_of_relevant_data = data['results']['books']
    book_list = []

    for book in the_list_of_relevant_data:
        book_list.append(
            {
                'title': book['title'],
                'author': book['author'],
                'publisher': book['publisher'],
                'description': book['description'],
                'weeks_on_list': book['weeks_on_list'],
                'rank': book['rank'],
                'rank_last_week': book['rank_last_week'],
            }
        )

    return book_list

fiction_book_list = create_book_list(NYT_bestsellers_fiction_API)
nonfiction_book_list = create_book_list(NYT_bestsellers_nonfiction_API)

print(fiction_book_list)
print(nonfiction_book_list)