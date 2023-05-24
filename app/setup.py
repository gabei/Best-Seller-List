from dotenv import load_dotenv
import os
import doc_builder as docbuilder
import call_api as API_CALLER


load_dotenv()
NYT_bestsellers_fiction_API = os.getenv("BOOKS_API_FICTION")
NYT_bestsellers_nonfiction_API = os.getenv("BOOKS_API_NONFICTION")

fiction_book_list = API_CALLER.create_book_list(NYT_bestsellers_fiction_API)
nonfiction_book_list = API_CALLER.create_book_list(NYT_bestsellers_nonfiction_API)


# Build the Word Document
doc = docbuilder.DocBuilder()
doc.set_document_default_font_and_size("Arial", 10)
doc.create_header("New York Times Best Seller List")

# Adjust Margins
margin_list_inches = [0.5, 0.5, 0.5, 0.5]
doc.define_margins_inches(margin_list_inches)

# Setup the Table
doc.create_table(1, 4) #create an intial table with enough columns for headers
doc.table.allow_autofit = True
table_headers = ['This Week', 'Description', 'Last Week', 'Weeks on List']
doc.create_headers_for_table(table_headers)

# Populate the Table
for book in fiction_book_list:
    #print(book)
    #print("\n")
    doc.build_row_from(book)

# Apply Column Widths
column_widths_inches = [0.5, 7, 0.6, 0.7]
doc.set_column_widths_inches(column_widths_inches)
doc.save_document('test')