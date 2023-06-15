from document_factory.document_block_handlers.paragraph_creator import ParagraphCreator
from document_factory.document_block_handlers.text_creator import TextCreator
from docx import Document


class HeadingCreator:
    """Умеет создавать различные заголовки"""

    @staticmethod
    def create_heading_by_parameters(
            document: Document, text: str, style_paragraph: dict = None, style_text: dict = None
    ):
        """Создать заголовок по переданным параметрам"""
        heading = ParagraphCreator.create_empty_paragraph(document)
        text = heading.add_run(text)
        ParagraphCreator.set_style_for_paragraph(heading, style_paragraph)
        TextCreator.set_text_style_by_parameters(text, style_text)

    def create_custom_main_heading(self, document: Document, data):
        """Создает главный заголовок для документа(заголовок в самом начале документа)"""
        text_by_heading = data.get('content')
        style_by_paragraph = data.get('style').get('style_by_paragraph')
        style_by_text = data.get('style').get('style_by_text')
        self.create_heading_by_parameters(document, text_by_heading, style_by_paragraph, style_by_text)
