# Best-Seller-List
A quick app to call the NYT Book API and generate a neatly ordered word doc for a public library display.

### Installation
```pip install -r requirements.txt``` 

then 

```pip install python-docx```<br>
```pip install requests```<br>
```pip install python-dotenv```<br>

This application makes use of the <a href="https://developer.nytimes.com/docs/books-product/1/overview">New York Times Books API</a>. You need an API key from NYT to use in your environment variables (hidden). Environment variables should be stored in a ```.env``` file of your creation. 

Your ```.env``` file should look like this: <br>

```BOOKS_API_KEY=YOURAPIKEY```<br>
```BOOKS_API_FICTION=https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction?api-key=${BOOKS_API_KEY}```<br>
```BOOKS_API_NONFICTION=https://api.nytimes.com/svc/books/v3/lists/current/hardcover-nonfiction?api-key=${BOOKS_API_KEY}```<br>

### Running the Application
To run the application, open a terminal or cmd line in the root folder (/Best-Sellers-List) and run ```py .\app\app.py```.<br>
This will generate two docx files - one a fiction book list and the other a nonfiction book list.
