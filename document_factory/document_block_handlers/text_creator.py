from docx.enum.text import *
from docx.shared import *


class TextCreator:
    """Умеет создавать тест для со стилями для параграфов и таблиц и заголовков"""

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
