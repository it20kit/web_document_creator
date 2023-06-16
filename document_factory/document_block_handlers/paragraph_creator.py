from docx import Document
from docx.shared import *
from docx.enum.text import *


class ParagraphCreator:
    """Умеет создавать параграфы для документа со стилями"""
    alignment: dict = {
        "WD_PARAGRAPH_ALIGNMENT.CENTER": WD_PARAGRAPH_ALIGNMENT.CENTER,
        "WD_PARAGRAPH_ALIGNMENT.LEFT": WD_PARAGRAPH_ALIGNMENT.LEFT,
        "WD_PARAGRAPH_ALIGNMENT.RIGHT": WD_PARAGRAPH_ALIGNMENT.RIGHT
    }

    @staticmethod
    def create_empty_paragraph(document: Document):
        """Создает пустой абзац"""
        return document.add_paragraph("")

    @staticmethod
    def create_numbered_list_paragraph(document: Document):
        return document.add_paragraph("", style="List Number")

    @staticmethod
    def set_style_for_paragraph(paragraph, style: dict = None):
        """Установить стиль для абзаца"""
        if style is not None:
            alignment = style.get('alignment')
            if alignment is not None:
                alignment = ParagraphCreator.alignment[alignment]
                paragraph.paragraph_format.alignment = alignment
            indent = style.get('indent')
            if indent is not None:
                indent_size = Inches(indent)
                paragraph.paragraph_format.left_indent = indent_size
