from document_factory.document_creators.abstract_document_creator import AbstractDocumentCreator
from document_factory.factory.document_name_factory import DocumentNameFactory
from document_factory.document_descriptor import DocumentDescriptor


class DocumentManager:
    """Умеет создавать документы в зависимости от переданного класса creatorDocx"""

    @staticmethod
    def create_document(abstract_creator: AbstractDocumentCreator, form: dict):
        """Создание нужного документа в зависимости от creatorDocx"""
        document = abstract_creator.create_document(form)
        document_name = DocumentNameFactory().create_name_for_document(form)
        return DocumentDescriptor(document_name, document)
