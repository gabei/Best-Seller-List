from docx import Document


class DocBuilder:
    """This class is used to organize methods related to .docx document creation. Upon initialization, it creates its own document using the docx module."""

    def __init__(self):
        self.doc = Document()

    def build_header_text(self, text):
        """Builds a document header using the passed text.
        - Expects a string
        - Returns 1 if successful."""

        if type(text) is not str:
            raise TypeError("This method only accepts strings.")

        self.doc.add_heading(text)
        self.doc.add_page_break()
        return 1
    
    def create_table(self, rows=0, cols=0):
        """
        Creates a table of specified rows and columns. Creates a blank table if not specified.
        - Expects integers > 0 for rows and cols
        - Invalid input will create a blank table
        - Returns 1 if successful
        """
        pass

    def build_row_from(data):
        """Builds a row of table data using the data passed.
        - Expects an array in desired order"""

        row = self.table.add_row()

       # for item in data:


        pass