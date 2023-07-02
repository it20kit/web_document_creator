from docx.shared import *
from docx import Document


class DocumentStandardizer:
    """Умеет задавать стандарты для всего документа"""

    @staticmethod
    def set_padding_sizes_for_all_document(document: Document, data: dict) -> None:
        """Добавить отступы для всего документа"""
        section = document.sections[0]
        bottom = data.get('bottom')
        if bottom is not None:
            section.bottom_margin = Mm(bottom)
        top = data.get('top')
        if top is not None:
            section.top_margin = Mm(top)
        right = data.get('right')
        if right is not None:
            section.right_margin = Mm(right)
        left = data.get('left')
        if left is not None:
            section.left_margin = Mm(left)

    @staticmethod
    def set_style_standard_for_all_document(document: Document, data: dict) -> None:
        """Задать стиль для всего документа(размер и стиль шрифта)"""
        style = document.styles["Normal"]
        font_name = data.get('font_name')
        if font_name is not None:
            style.font.name = font_name
        text_size = data.get('text_size')
        if text_size is not None:
            style.font.size = Pt(text_size)
