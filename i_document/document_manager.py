from i_document.document_descriptor import DocumentDescriptor
from i_document.creators.abstract_document_creator import AbstractDocumentCreator


class DocumentManager:
    """Умеет создавать и сохранять документы, в зависимости от переданного класса creatorDocx"""

    def __init__(self, path: str):
        self.path_to_save = path

    def create_document(self, abstract_creator: AbstractDocumentCreator, data: object):
        """Создание нужного документа в зависимости от creatorDocx"""
        descriptor = abstract_creator.create_document(data)
        self.__save_document(descriptor)
        return self.path_to_save + descriptor.document_name

    def __save_document(self, descriptor: DocumentDescriptor):
        """Сохранить документ в переданной директории"""
        descriptor.document.save(
            self.path_to_save +
            descriptor.document_name
        )
