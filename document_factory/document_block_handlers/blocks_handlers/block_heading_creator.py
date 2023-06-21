from docx import Document
from document_factory.document_block_handlers.blocks_handlers.abstract_block_creator import AbstractBlockCreator


class HeadingCreator(AbstractBlockCreator):
    """Умеет создавать различные заголовки"""

    def create_blog_based_on_data(self, document: Document, data: dict):
        """Умеет создавать заголовки по типу заголовка"""
        type_heading = self.__get_type_heading(data)
        if type_heading == 'numbered_list':
            self.create_numbered_list_heading(document, data)
        elif type_heading == 'regular heading':
            self.create_regular_heading(document, data)
        elif type_heading == 'empty heading':
            self.create_empty_paragraph(document)
        else:
            raise TypeError("Invalid heading type in JSON template")

    def create_custom_main_heading(self, heading, data: dict) -> None:
        """Создает главный заголовок для документа(заголовок в самом начале документа)"""
        text_by_heading = data.get('content')
        style = data.get('parameters').get('style')
        self.add_content_in_paragraph(heading, text_by_heading, style)

    def create_numbered_list_heading(self, document: Document, data: dict) -> None:
        heading = self.create_empty_numbered_list_paragraph(document)
        self.create_custom_main_heading(heading, data)

    def create_regular_heading(self, document: Document, data: dict) -> None:
        heading = self.create_empty_paragraph(document)
        self.create_custom_main_heading(heading, data)

    @staticmethod
    def __get_type_heading(block: dict):
        type_block = block.get('parameters').get('type_heading')
        if type_block is None:
            raise KeyError('incorrect structure of the json document description')
        return type_block
