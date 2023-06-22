from document_factory.document_block_handlers.blocks_handlers.block_heading_creator import HeadingCreator
from document_factory.document_block_handlers.blocks_handlers.block_paragraph_creator import BlockParagraphCreator
from document_factory.document_block_handlers.blocks_handlers.block_table_creator import TableCreator


class BlockHandlerManager:
    """Знает как создавать по переданному типу"""

    def __init__(self):
        self.config_container = [
            "HeadingCreator",
            "TableCreator",
            "BlockParagraphCreator"
        ]

    def get_handler_by_block_type(self, block_type: str):
        """Вызывает нужный обработчик для блока по типу блока документа"""
        self.__check_if_there_is_handler_in_container(block_type)
        return globals()[block_type]().create_block_based_on_data

    def __check_if_there_is_handler_in_container(self, block_type: str) -> None:
        """Проверить есть ли обработчик для блока в контейнере"""
        if self.__is_there_such_handler_in_container(block_type) is False:
            raise TypeError("handler not found")

    def __is_there_such_handler_in_container(self, block_type) -> bool:
        """Проверяет блок в контейнере"""
        for handler in self.config_container:
            if handler == block_type:
                return True
        return False
