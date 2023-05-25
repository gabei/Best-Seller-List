import requests

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
    - Returns a a dict containing the list and the book list itself as a list of dictionaries.
    """

    data = call_api_and_get_json_data(API_URL)
    the_list_of_relevant_data = data['results']['books']
    list_name = data['results']['list_name']
    list_date = data['results']['published_date']
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

    return {
        "list_name": list_name,
        "list_date": list_date,
        "book_list": book_list
    }
    