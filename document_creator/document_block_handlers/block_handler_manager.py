from document_creator.document_block_handlers.blocks_handlers.block_heading_creator import HeadingCreator
from document_creator.document_block_handlers.blocks_handlers.block_paragraph_creator import ParagraphCreator
from document_creator.document_block_handlers.blocks_handlers.block_table_creator import TableCreator


class BlockHandlerManager:
    """Знает как создавать по переданному типу"""

    def __init__(self):
        self.config_container = {
            "HeadingCreator": HeadingCreator(),
            "TableCreator": TableCreator(),
            "BlockParagraphCreator": ParagraphCreator()
        }

    def get_handler_by_block_type(self, block_type: str):
        """Вызывает нужный обработчик для блока по типу блока документа"""
        self.__check_handler_in_container(block_type)
        return self.config_container.get(block_type).create_block_based_on_data

    def __check_handler_in_container(self, block_type: str) -> None:
        """Проверить есть ли обработчик для блока в контейнере"""
        if self.config_container.get(block_type) is None:
            raise KeyError("The handler for the block was not found in the container")
