from document_factory.document_block_handlers.table_creator import TableCreator
from docx import Document
from document_factory.document_block_handlers.heading_creator import HeadingCreator


class BlockCreatorManager:
    """Знает как создавать по переданному типу"""

    def __init__(self):
        self.handler = {
            "create_table_two_columns": self.create_table_two_columns,
            "create_custom_main_heading": self.create_custom_main_heading,
        }

    def get_block_creators_by_type(self, block_type):
        return self.handler.get(block_type)

    @staticmethod
    def create_table_two_columns(document: Document(), data: dict):
        TableCreator().create_table_two_columns(document, data)

    @staticmethod
    def create_custom_main_heading(document: Document, data):
        HeadingCreator().create_custom_main_heading(document, data)
