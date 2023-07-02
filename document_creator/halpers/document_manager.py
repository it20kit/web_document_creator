from document_creator.halpers.document_name_manager import DocumentNameManager
from document_creator.halpers.document_descriptor import DocumentDescriptor
from docx import Document
from document_creator.document_block_handlers.block_handler_manager import BlockHandlerManager
from document_creator.document_block_handlers.tools.document_standardizer import DocumentStandardizer
from document_creator.halpers.document_structure_manager import DocumentStructureManager


class DocumentManager:
    """Умеет создавать документы в зависимости от переданного класса creatorDocx"""

    def __init__(self):
        self.document_structure_manager = DocumentStructureManager()

    def create_document(self, form: dict):
        """Создание нужного документа в зависимости от creatorDocx"""
        document = self.create_document_from_form(form)
        document_name = DocumentNameManager().create_name_for_document(form)
        return DocumentDescriptor(document_name, document)

    def create_document_from_form(self, form: dict) -> Document:
        """Создать документ из формы и обернуть его в дескриптор"""
        document = Document()
        description = self.__get_description_document_from_form(form)
        block_document = self.__get_block_document_from_form(form)
        if self.document_structure_manager.get_standard_styles_for_document(form) is not None:
            style = self.document_structure_manager.get_standard_styles_for_document(form)
            self.__set_standard_for_all_document(document, style)
        for block in block_document:
            block_title = self.__get_block_title(block)
            if block_title is not None:
                self.__process_block_styles(description, block_title)
                self.__add_block(document, block_title)
            subblocks = self.__get_subblock_from_block(block)
            if subblocks is not None:
                for blocks in subblocks:
                    self.__process_block_styles(description, blocks)
                    self.__add_block(document, blocks)
        return document

    def __add_block(self, document: Document, block: dict):
        block_type = self.document_structure_manager.get_type_of_block_handler(block)
        block_creator = BlockHandlerManager().get_handler_by_block_type(block_type)
        block_creator(document, block)

    def __process_block_styles(self, description: dict, block: dict):
        if self.__does_block_have_styles(block):
            list_styles = self.__get_list_styles_by_block_from_description(description, block)
            self.__replace_block_styles(list_styles, block)

    def __get_block_title(self, block: dict):
        return self.document_structure_manager.get_title_block_from_block(block)

    def __get_subblock_from_block(self, block: dict):
        return self.document_structure_manager.get_subblock_from_block(block)

    def __set_standard_for_all_document(self, document: Document, style: dict) -> None:
        """Установить стандарты для всего документа(размер шрифта, отступы и т.д)"""
        margins = self.document_structure_manager.get_margins_sizes_from_standard_style(style)
        style = self.document_structure_manager.get_style_from_standard_style(style)
        DocumentStandardizer.set_style_standard_for_all_document(document, style)
        DocumentStandardizer.set_padding_sizes_for_all_document(document, margins)

    def __get_description_document_from_form(self, form: dict) -> dict:
        description = self.document_structure_manager.get_description_document(form)
        if description is None:
            raise KeyError('Incorrect json structure')
        return description

    def __get_block_document_from_form(self, form: dict) -> list:
        block = self.document_structure_manager.get_block_from_template(form)
        if block is None:
            raise KeyError("Incorrect json structure or missing document creation blocks")
        return block

    def __get_style_by_block_from_block(self, block: dict) -> list:
        if self.document_structure_manager.get_style_from_block(block) is None:
            raise ValueError('The name of the style class for the block is missing')
        return self.document_structure_manager.get_style_from_block(block)

    def get_style_by_name_class_from_description(self, description: dict, name_class: str) -> dict:
        style = self.document_structure_manager.get_classes_style_from_style(description).get(name_class)
        if style is None:
            raise KeyError('The name of the style class was not found')
        return style

    def __does_block_have_styles(self, block: dict) -> bool:
        return self.document_structure_manager.get_style_from_block(block) is not None

    def __get_list_styles_by_block_from_description(self, description: dict, block: dict) -> list:
        list_style = []
        list_of_block_style_names = self.__get_style_by_block_from_block(block)
        for name_class_style in list_of_block_style_names:
            style = self.get_style_by_name_class_from_description(description, name_class_style)
            list_style.append(style)
        return list_style

    @staticmethod
    def __replace_block_styles(list_style: list, block: dict) -> None:
        block['parameters']['style'] = list_style
