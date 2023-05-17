from dotenv import load_dotenv
import os
import requests


load_dotenv()
NYT_bestsellers_fiction_API = os.getenv("BOOKS_API_FICTION")
NYT_bestsellers_nonfiction_API = os.getenv("BOOKS_API_NONFICTION")


def get_list(API_URL):
    r = requests.get(API_URL)
    the_list = r.json()['results']['books']

    print('Rank\tTitle\tAuthor\tWeeks on List')

    for book in the_list:
        title = book['title']
        author = book['author']
        rank = book['rank']
        weeks_on_list = book['weeks_on_list']

        print(f'{rank}\t{title}\t\t\t\t{author}\t{weeks_on_list}')
    print("\n")


get_list(NYT_bestsellers_fiction_API)
get_list(NYT_bestsellers_nonfiction_API)
