from document_factory.document_block_handlers.tools.paragraph_tool import ParagraphTool
from document_factory.document_block_handlers.tools.text_style_tool import TextTool
from docx import Document


class BlockParagraphCreator:
    """Умеет создавать абзацы теста от переданных параметров"""

    def create_custom_paragraph(self, document: Document, data: dict):
        ParagraphTool.set_style_for_paragraph(data.get('parameters').get('style').get('style_by_paragraph'))
        self.add_data_custom_paragraph(document, data)

    def add_data_custom_paragraph(self, document, data: dict):
        """Создает абзац, где часть теста с нижним подчеркиванием, а остальная часть без"""
        a = data.get('content')
        style_for_text = data.get('parameters').get('style').get('style_by_first_text')
        style_for_text2 = data.get('parameters').get('style').get('style_by_second_text')
        for i in range(len(a)):
            paragraph = ParagraphTool.create_empty_paragraph(document)
            ParagraphTool.set_style_for_paragraph(paragraph, data.get('parameters').get('style').get('style_by_paragraph'))
            translation = a[i].get('translation')
            value = a[i].get('value')
            self.add_content_for_custom_paragraph(paragraph, translation, style_for_text)
            if value != "{{ }}":
                self.add_content_for_custom_paragraph(paragraph, value, style_for_text2)

    @staticmethod
    def add_content_for_custom_paragraph(paragraph, text, style_for_text: dict):
        text = paragraph.add_run(text)
        TextTool.set_text_style_by_parameters(text, style_for_text)
