from docx import Document
from document_factory.document_block_handlers.blocks_handlers.abstract_block_creator import AbstractBlockCreator


class BlockParagraphCreator(AbstractBlockCreator):
    """Умеет создавать абзацы теста от переданных параметров"""

    def create_block_based_on_data(self, document: Document, data: dict) -> None:
        contents = self.get_content_block_from_data(data)
        style = self.get_style_block_from_data(data)
        for content in contents:
            if self.are_there_empty_values_in_content(content) is False:
                self.__processing_content(document, content, style)

    @staticmethod
    def __add_content_for_paragraph(paragraph, text: str, style_for_text: dict) -> None:
        """Добавить текст в абзац и применить е нему стиль"""
        text = paragraph.add_run(text)
        AbstractBlockCreator.StyleManager.set_text_style_by_parameters(text, style_for_text)

    def __processing_content(self, document, content: dict, style: dict) -> None:
        """Собрать из контента параграф с разными стилями текста"""
        style_by_content = style.get('style_by_content')
        style_by_paragraph = style.get('style_by_paragraph')
        paragraph = self.create_empty_paragraph(document)
        AbstractBlockCreator.StyleManager.set_style_for_paragraph(paragraph, style_by_paragraph)
        for i in range(len(content)):
            style_by_value = style_by_content[i]
            self.__add_content_for_paragraph(paragraph, content[i], style_by_value)
