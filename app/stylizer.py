from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Pt, Inches

'''
TODO
- DRY
- Fix up some of the repeated assignments in this module
- Errors
'''


def style_ranking_numbers(rank: str) -> str:
    """
    Styles the rank number text

    Expects: Strings containing numbers
    Returns: 0s as "--" and all other numbers the same
    """

    if rank != '0':
        return rank
    
    return '--'

def set_cell_font_size(cell, font_size: int):
    """
    Sets cell paragraph's font size.

    Expects: Integer > 0
    Returns: 1 if updated successfully
    """

    text = cell.paragraphs[0]
    text.style.font.size = Pt(font_size)

    return 1

def center_cell_text(cell):
    """
    Applies center styling to inner-cell text.

    Expects: Reference to cell
    Returns: Nothing. Alters the cell's text
    """

    text = cell.paragraphs[0]
    text.alignment = WD_TABLE_ALIGNMENT.CENTER

    return 1

def bolden_cell_text(cell):

    cell.paragraphs[0].runs[0].font.bold = True
    return 1