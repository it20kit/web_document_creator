from abc import ABC, abstractmethod
from docx import Document
from document_factory.document_descriptor import DocumentDescriptor


class AbstractDocumentCreator(ABC):
    """Задаёт абстракцию для всех наследуемых creatorDocx"""

    @abstractmethod
    def create_document(self, data: dict) -> Document():
        """Создать документ"""
        pass

    @abstractmethod
    def add_block(self, document: Document, block: dict):
        """Добавляет блоки с контентом в документ"""
        pass
