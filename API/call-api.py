from dotenv import load_dotenv
import os
import requests

load_dotenv()

apikey = os.getenv("BOOKS_API_FULL_URL")
print(apikey)
