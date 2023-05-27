import doc_builder as docbuilder
import stylizer
import settings


def generate_NYT_best_seller_doc(book_api: dict) -> docbuilder:
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
    doc = docbuilder.DocBuilder()
    doc.set_document_default_font_and_size(font, font_size)
    doc.create_header(document_heading)
    doc.define_margins_inches(margin_list_inches)

    return doc

def build_docx_table(doc, book_api, table_rows_cols, table_allow_autofit) -> int:

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

    return 1

def populate_docx_table(doc: docbuilder, book_api: dict, column_widths) -> int:

    for book in book_api["book_list"]:
        doc.build_row_from(book)

    # Adjust column widths after filling
    doc.set_column_widths_inches(column_widths)

    return 1

def save_document(doc, title):
    print(doc.save_document(title))
    return doc