from document_factory.creators.abstract_document_creator import AbstractDocumentCreator


class DocumentManager:
    """Умеет создавать документы в зависимости от переданного класса creatorDocx"""

    def __init__(self):
        pass

    def create_document(self, abstract_creator: AbstractDocumentCreator, form: dict):
        """Создание нужного документа в зависимости от creatorDocx"""
        return abstract_creator.create_document(form)
