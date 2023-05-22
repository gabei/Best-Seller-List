from dotenv import load_dotenv
import os
import requests
import doc_builder as docbuilder


def call_api_and_get_json_data(API_URL: str) -> dict:
    """
    Calls the NYT Best Seller API and returns the raw JSON data.
    - Expects a valid api URL with api key included
    - Returns data in json format
    """

    r = requests.get(API_URL)
    return r.json()


def create_book_list(API_URL: str) -> list:
    """
    Takes NYT best seller data as json data, grabs the relevant info, and creates a new list of stripped down data to return.
    - Expects a valid api URL with api key included.
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


load_dotenv()
NYT_bestsellers_fiction_API = os.getenv("BOOKS_API_FICTION")
NYT_bestsellers_nonfiction_API = os.getenv("BOOKS_API_NONFICTION")

fiction_book_list = create_book_list(NYT_bestsellers_fiction_API)
nonfiction_book_list = create_book_list(NYT_bestsellers_nonfiction_API)


# Build the Word Document
doc = docbuilder.DocBuilder()
doc.create_header("New York Times Best Seller List")

# Check that it worked
print(doc)

# Setup the Table
doc.create_table(16, 4)
table_headers = ['Rank', 'Description', 'Last Week', 'Weeks on List']
doc.create_headers_for_table(table_headers)

# Populate the Table
for book in fiction_book_list:
    #print(book)
    #print("\n")
    doc.build_row_from(book)

doc.save_document('test')

