from document_factory.document_creators.abstract_document_creator import AbstractDocumentCreator
from docx import Document
from document_factory.document_block_handlers.block_handler_manager import BlockHandlerManager
from document_factory.document_block_handlers.tools.document_standardizer import DocumentStandardizer


class PsychologicalEvaluationCreatorDocx(AbstractDocumentCreator):
    """Создает docx документ с психологическим заключением ребёнка, по выбранным параметрам"""

    def create_document(self, form: dict) -> Document():
        """Создать документ психологической оценки и обернуть его в дескриптор"""
        document = Document()
        if form.get('standard_margins_and_styles_for_the_entire_document') is not None:
            self.__set_standard_for_all_document(document, form)
        for block in form['blocks']:
            self.add_block(document, block)
        return document

    def add_block(self, document: Document, block: dict):
        block_type = block.get('type')
        block_creator = BlockHandlerManager().get_block_creators_by_type(block_type)
        block_creator(document, block)

    @staticmethod
    def __set_standard_for_all_document(document: Document, form: dict) -> None:
        """Установить стандарты для всего документа(размер шрифта, отступы и т.д)"""
        margins = form.get('standard_margins_and_styles_for_the_entire_document').get('margins_sizes')
        style = form.get('standard_margins_and_styles_for_the_entire_document').get('style')
        DocumentStandardizer.set_style_standard_for_all_document(document, style)
        DocumentStandardizer.set_padding_sizes_for_all_document(document, margins)
