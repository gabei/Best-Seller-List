from docx import Document


class DocBuilder:
    """This class is used to organize methods related to .docx document creation. Upon initialization, it creates its own document using the docx module."""

    def __init__(self):
        self.doc = Document()

    def create_header(self, text):
        """Builds a document header using the passed text.
        - Expects a string
        - Returns 1 if successful."""

        if type(text) is not str:
            raise TypeError("This method only accepts strings.")

        self.doc.add_heading(text)
        self.doc.add_page_break()
        self.title = text
        return 1

    def create_table(self, r: int, c: int):
        """
        Creates a table of specified rows and columns. Creates a blank table if not specified.
        - Expects integers > 0 for rows and cols
        - Invalid input will create a blank table
        - Returns 1 if successful
        """
        self.table = self.doc.add_table(rows=r, cols=c)

        return 1

    def create_headers_for_table(self, header_list: list) -> None:
        # Define the headers in the table
        headers = self.table.rows[0].cells

        # Check for erroneous values
        if len(header_list) <= 0 or type(header_list) is not list:
            for index in range(0, len(headers)-1):
                headers[index].text = str(index + 1)

        # Fill in the headers if all is OK
        for index in range(0, len(header_list)-1):
            headers[index].text = header_list[index]

        return 1

    def build_row_from(data):
        """Builds a row of table data using the data passed.
        - Expects an array in desired order"""

        row = self.table.add_row()

       # for item in data:

        pass

    def save_document(self, file_name: str) -> str:
        self.doc.save(file_name+".docx")
        return f"Document saved at \"{file_name}.docx\""

    def __str__(self):
        return f"Document titled \"{self.title}\""
