import doc_builder as docbuilder
import stylizer
import settings


def generate_NYT_best_seller_doc(book_api: dict) -> docbuilder:
    """Entry point for this program. Harbors the function calls that build the NYT best seller list document.

    Expects: The relevant NYT Books Api information in json format.
    Returns: The document object.
    """

    print(f"Generating New York Times Best Seller List: {book_api['list_name']}")

    # Build the Word Document
    doc = build_docx(settings.FONT, settings.FONT_SIZE, settings.DOCUMENT_HEADING, settings.MARGIN_LIST_INCHES)

    # Build the table
    build_docx_table(doc, book_api, settings.TABLE_ROWS_COLS, settings.TABLE_ALLOW_AUTOFIT)
    populate_docx_table(doc, book_api, settings.COLUMN_WIDTHS_INCHES)

    # Save our work!
    title = f'NYT-BS-List_{book_api["list_name"]}_{book_api["list_date"]}'
    save_document(doc, title) 

    return doc

def build_docx(font: str, font_size: int, document_heading: str, margin_list_inches: list) -> docbuilder:
    """Creates the document object. This must happen first to perform any of the other document related functions.

    Expects: Font, font size, heading, margins
    ReturnsL The document object. 
    """

    doc = docbuilder.DocBuilder()
    doc.set_document_default_font_and_size(font, font_size)
    doc.create_header(document_heading)
    doc.define_margins_inches(margin_list_inches)

    return doc

def build_docx_table(doc, book_api, table_rows_cols, table_allow_autofit) -> None:
    """ Creates the table that will hold the NYT list.

    Expects: doc object, api info, rows, columns, table autofit bool
    Returns: Nothing. The table is created as a part of the document object. 
    """

    # create an intial table with enough columns for headers
    doc.create_table(table_rows_cols) 
    doc.table.allow_autofit = table_allow_autofit

    # Table name and date requires formatting
    list_namedate_header = stylizer.generate_namedate_header(
        book_api['list_date'],
        book_api['list_name']
    )
    header_list = ['This Week', list_namedate_header, 'Last Week', 'Weeks on List']
    doc.create_headers_for_table(header_list)

def populate_docx_table(doc: docbuilder, book_api: dict, column_widths) -> None:
    """ Populates the NYT table.

    Expects: doc object, api info, rows, columns widths
    Returns: Nothing. The table is created as a part of the document object.  
    """

    for book in book_api["book_list"]:
        doc.build_row_from(book)

    # Adjust column widths after filling
    doc.set_column_widths_inches(column_widths)

def save_document(doc, title):
    """ Save the document as docx filetype.

    Expects: doc object, the title
    Returns: The document. This is for use in other parts of the app.
    """

    print(doc.save_document(title))
    return doc