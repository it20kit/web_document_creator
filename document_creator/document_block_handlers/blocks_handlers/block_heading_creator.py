from docx import Document
from document_creator.document_block_handlers.blocks_handlers.abstract_block_creator import AbstractBlockCreator


class HeadingCreator(AbstractBlockCreator):
    """Умеет создавать различные заголовки"""

    def create_block_based_on_data(self, document: Document, data: dict) -> None:
        """Умеет создавать заголовки по типу заголовка"""
        type_heading = self.__get_type_heading(data)
        if type_heading == 'numbered_list':
            self.__create_numbered_list_heading(document, data)
        elif type_heading == 'regular_heading':
            self.__create_regular_heading(document, data)
        elif type_heading == 'empty_heading':
            self.create_empty_paragraph(document)
        elif type_heading == 'do_not_add_to_document':
            pass
        else:
            raise TypeError("Invalid heading type in JSON template")

    def __apply_styles_for_heading(self, heading, data: dict) -> None:
        """Применить стиль к заголовку"""
        content = self.document_structure_manager.get_content_from_block(data)
        texts_heading = self.get_value_from_content(content)
        style = self.document_structure_manager.get_style_from_block(data)
        for i in range(len(texts_heading)):
            text = texts_heading[i]
            style_by_heading = style[i]
            self.add_content_in_paragraph(heading, text, style_by_heading)

    def __create_numbered_list_heading(self, document: Document, data: dict) -> None:
        """Создает нумерованный заголовок"""
        heading = self.create_empty_numbered_list_paragraph(document)
        self.__apply_styles_for_heading(heading, data)

    def __create_regular_heading(self, document: Document, data: dict) -> None:
        """Создает обычный заголовок"""
        heading = self.create_empty_paragraph(document)
        self.__apply_styles_for_heading(heading, data)

    def __get_type_heading(self, block: dict) -> str:
        type_heading = self.document_structure_manager.get_type_block_from_block(block)
        print(type_heading)
        if type_heading is None:
            raise KeyError('incorrect structure of the json document description')
        return type_heading
