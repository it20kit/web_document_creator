from docx.shared import *
from docx.enum.text import *


class DocumentStyleManager:
    """Умеет задавать стили текста и стили абзацев"""
    alignment: dict = {
        "WD_PARAGRAPH_ALIGNMENT.CENTER": WD_PARAGRAPH_ALIGNMENT.CENTER,
        "WD_PARAGRAPH_ALIGNMENT.LEFT": WD_PARAGRAPH_ALIGNMENT.LEFT,
        "WD_PARAGRAPH_ALIGNMENT.RIGHT": WD_PARAGRAPH_ALIGNMENT.RIGHT
    }

    @staticmethod
    def set_style_for_paragraph(paragraph, style: dict = None):
        """Установить стиль для абзаца"""
        if style is not None:
            alignment = style.get('alignment')
            if alignment is not None:
                alignment = DocumentStyleManager.alignment[alignment]
                paragraph.paragraph_format.alignment = alignment
            indent = style.get('indent')
            if indent is not None:
                indent_size = Inches(indent)
                paragraph.paragraph_format.left_indent = indent_size

    @staticmethod
    def set_text_style_by_parameters(text, style: dict = None) -> None:
        """Задать стиль текста по заданным параметрам(размер текста, жирный, подчеркнутый или курсив"""
        if style is not None:
            text_size = style.get('text_size')
            if text_size is not None:
                text.font.size = Pt(text_size)
            are_bold = style.get('are_bold')
            if are_bold is not None:
                text.font.bold = are_bold
            are_italic = style.get('are_italic')
            if are_italic is not None:
                text.font.italic = are_italic
            are_underline = style.get('are_underline')
            if are_underline is not None:
                text.font.underline = WD_UNDERLINE.SINGLE
            font_name = style.get('font_name')
            if font_name is not None:
                text.font.name = font_name
