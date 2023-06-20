from document_factory.document_block_handlers.tools.paragraph_tool import ParagraphTool
from document_factory.document_block_handlers.tools.text_style_tool import TextTool
from docx import Document
from document_factory.document_block_handlers.blocks_handlers.abstract_block_creator import AbstractBlockCreator


class BlockParagraphCreator(AbstractBlockCreator):
    """Умеет создавать абзацы теста от переданных параметров"""

    def create_block(self, document: Document, data: dict) -> None:
        contents = data.get('content')
        style = data.get('parameters').get('style')
        for content in contents:
            if self.are_there_empty_values_in_content(content) is False:
                self.processing_content(document, content, style)

    @staticmethod
    def add_content_for_paragraph(paragraph, text, style_for_text: dict):
        text = paragraph.add_run(text)
        TextTool.set_text_style_by_parameters(text, style_for_text)

    def processing_content(self, document, content: dict, style: dict):
        style_by_content = style.get('style_by_content')
        style_by_paragraph = style.get('style_by_paragraph')
        paragraph = ParagraphTool.create_empty_paragraph(document)
        ParagraphTool.set_style_for_paragraph(paragraph, style_by_paragraph)
        for i in range(len(content)):
            style_by_value = style_by_content[i]
            self.add_content_for_paragraph(paragraph, content[i], style_by_value)
