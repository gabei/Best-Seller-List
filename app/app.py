from dotenv import load_dotenv
import os
import call_api as API_CALLER
import generate

load_dotenv()
NYT_bestsellers_fiction_API = os.getenv("BOOKS_API_FICTION")
NYT_bestsellers_nonfiction_API = os.getenv("BOOKS_API_NONFICTION")

fiction_book_list = API_CALLER.create_book_list(NYT_bestsellers_fiction_API)
nonfiction_book_list = API_CALLER.create_book_list(NYT_bestsellers_nonfiction_API)

fiction_document = generate.generate_NYT_best_seller_doc(fiction_book_list)
nonfiction_document = generate.generate_NYT_best_seller_doc(nonfiction_book_list)