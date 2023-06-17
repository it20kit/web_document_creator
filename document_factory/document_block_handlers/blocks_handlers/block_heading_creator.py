from document_factory.document_block_handlers.tools.paragraph_tool import ParagraphTool
from document_factory.document_block_handlers.tools.text_style_tool import TextTool
from docx import Document


class HeadingCreator:
    """Умеет создавать различные заголовки"""

    @staticmethod
    def apply_styles_to_heading(
            heading, text: str, style_paragraph: dict = None, style_text: dict = None
    ):
        """Создать заголовок по переданным параметрам"""
        text = heading.add_run(text)
        ParagraphTool.set_style_for_paragraph(heading, style_paragraph)
        TextTool.set_text_style_by_parameters(text, style_text)

    def create_custom_main_heading(self, heading, data: dict) -> None:
        """Создает главный заголовок для документа(заголовок в самом начале документа)"""
        text_by_heading = data.get('content')
        style_by_paragraph = data.get('parameters').get('style').get('style_by_paragraph')
        style_by_text = data.get('parameters').get('style').get('style_by_text')
        self.apply_styles_to_heading(heading, text_by_heading, style_by_paragraph, style_by_text)

    @staticmethod
    def create_empty_heading(document: Document) -> None:
        ParagraphTool.create_empty_paragraph(document)

    def create_numbered_list_heading(self, document: Document, data: dict) -> None:
        heading = ParagraphTool.create_numbered_list_paragraph(document)
        self.create_custom_main_heading(heading, data)

    def create_regular_heading(self, document: Document, data: dict) -> None:
        heading = ParagraphTool.create_empty_paragraph(document)
        self.create_custom_main_heading(heading, data)