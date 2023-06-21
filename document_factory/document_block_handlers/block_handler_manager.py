from document_factory.document_block_handlers.blocks_handlers.block_table_creator import TableCreator
from docx import Document
from document_factory.document_block_handlers.blocks_handlers.block_heading_creator import HeadingCreator
from document_factory.document_block_handlers.blocks_handlers.block_paragraph_creator import BlockParagraphCreator


class BlockHandlerManager:
    """Знает как создавать по переданному типу"""

    def __init__(self):
        self.handler = {
            "TableCreator": self.create_table_two_columns,
            "HeadingCreator": self.create_regular_heading,
            "BlockParagraphCreator": self.create_custom_paragraph
        }

    def get_block_creators_by_type(self, block_type):
        return self.handler.get(block_type)

    @staticmethod
    def create_table_two_columns(document: Document, data: dict):
        TableCreator().create_blog_based_on_data(document, data)

    @staticmethod
    def create_regular_heading(document: Document, data: dict):
        HeadingCreator().create_blog_based_on_data(document, data)

    @staticmethod
    def create_numbered_list_heading(document: Document, data: dict):
        HeadingCreator().create_numbered_list_heading(document, data)

    @staticmethod
    def create_custom_paragraph(document: Document, data: dict):
        BlockParagraphCreator().create_blog_based_on_data(document, data)
