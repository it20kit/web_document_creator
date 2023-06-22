from docx import Document
from document_factory.document_block_handlers.blocks_handlers.abstract_block_creator import AbstractBlockCreator


class HeadingCreator(AbstractBlockCreator):
    """Умеет создавать различные заголовки"""

    def create_block_based_on_data(self, document: Document, data: dict) -> None:
        """Умеет создавать заголовки по типу заголовка"""
        type_heading = self.__get_type_heading(data)
        if type_heading == 'numbered_list':
            self.__create_numbered_list_heading(document, data)
        elif type_heading == 'regular heading':
            self.__create_regular_heading(document, data)
        elif type_heading == 'empty heading':
            self.create_empty_paragraph(document)
        else:
            raise TypeError("Invalid heading type in JSON template")

    def __apply_styles_for_heading(self, heading, data: dict) -> None:
        """Применить стиль к заголовку"""
        text_by_heading = self.get_content_block_from_data(data)
        style = self.get_style_block_from_data(data)
        self.add_content_in_paragraph(heading, text_by_heading, style)

    def __create_numbered_list_heading(self, document: Document, data: dict) -> None:
        """Создает нумерованный заголовок"""
        heading = self.create_empty_numbered_list_paragraph(document)
        self.__apply_styles_for_heading(heading, data)

    def __create_regular_heading(self, document: Document, data: dict) -> None:
        """Создает обычный заголовок"""
        heading = self.create_empty_paragraph(document)
        self.__apply_styles_for_heading(heading, data)

    @staticmethod
    def __get_type_heading(block: dict) -> str:
        type_heading = block.get('parameters').get('type_heading')
        if type_heading is None:
            raise KeyError('incorrect structure of the json document description')
        return type_heading
