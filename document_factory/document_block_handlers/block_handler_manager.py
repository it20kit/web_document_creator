from document_factory.document_block_handlers.table_creator import TableCreator
from docx import Document
from document_factory.document_block_handlers.heading_creator import HeadingCreator
from document_factory.document_block_handlers.block_paragraph_creator import BlockParagraphCreator


class BlockHandlerManager:
    """Знает как создавать по переданному типу"""

    def __init__(self):
        self.handler = {
            "create_table_two_columns": self.create_table_two_columns,
            "create_regular_heading": self.create_regular_heading,
            "create_numbered_list_heading": self.create_numbered_list_heading,
            "empty_string": self.empty_string,
            "create_custom_paragraph": self.create_custom_paragraph
        }

    def get_block_creators_by_type(self, block_type):
        return self.handler.get(block_type)

    @staticmethod
    def create_table_two_columns(document: Document, data: dict):
        TableCreator().create_table_two_columns(document, data)

    @staticmethod
    def create_regular_heading(document: Document, data: dict):
        HeadingCreator().create_regular_heading(document, data)

    @staticmethod
    def create_numbered_list_heading(document: Document, data: dict):
        HeadingCreator().create_numbered_list_heading(document, data)

    @staticmethod
    def empty_string(document: Document, data: dict):
        HeadingCreator.create_empty_heading(document)

    @staticmethod
    def create_custom_paragraph(document: Document, data: dict):
        BlockParagraphCreator().create_custom_paragraph(document, data)
