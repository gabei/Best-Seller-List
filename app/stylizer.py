from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.shared import Pt, Inches


def style_ranking_numbers(rank: str) -> str:
    """
    Styles the rank number text

    Expects: Strings containing numbers
    Returns: 0s as "--" and all other numbers the same
    """

    if rank != '0':
        return rank
    
    return '--'


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