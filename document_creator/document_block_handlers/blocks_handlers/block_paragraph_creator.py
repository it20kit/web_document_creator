from docx import Document
from document_creator.document_block_handlers.blocks_handlers.abstract_block_creator import AbstractBlockCreator


class ParagraphCreator(AbstractBlockCreator):
    """Умеет создавать абзацы теста от переданных параметров"""

    def create_block_based_on_data(self, document: Document, data: dict) -> None:
        contents = self.document_structure_manager.get_content_from_block(data)
        style = self.document_structure_manager.get_style_from_block(data)
        for content in contents:
            content = self.get_value_from_content(content)
            if self.are_there_empty_values_in_content(content) is False:
                self.__processing_content(document, content, style)

    def __processing_content(self, document: Document, content: dict, style: list) -> None:
        """Собрать из контента параграф с разными стилями текста"""
        paragraph = self.create_empty_paragraph(document)
        for i in range(len(content)):
            if i < len(style):
                style_by_paragraph = style[i]
            else:
                style_by_paragraph = {}
            self.add_content_in_paragraph(paragraph, content[i], style_by_paragraph)
