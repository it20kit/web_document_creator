from abc import ABC, abstractmethod
from docx import Document
from document_factory.document_descriptor import DocumentDescriptor


class AbstractDocumentCreator(ABC):
    """Задаёт абстракцию для всех наследуемых creatorDocx"""

    @abstractmethod
    def create_document(self, data: dict) -> DocumentDescriptor:
        """Создать документ"""
        pass

    @abstractmethod
    def create_name_document(self, data: dict) -> str:
        """Создать имя документа"""
        pass

    @abstractmethod
    def save(self, document: Document, name: str) -> None:
        """Сохранить документ"""
        pass
