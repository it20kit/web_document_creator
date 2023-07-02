from document_creator.halpers.document_manager import DocumentManager
from document_creator.halpers.document_descriptor import DocumentDescriptor


class DocumentCreator:
    """Библиотека умеющая создавать нужные документы"""

    def __init__(self, path):
        self.path_to_save = path
        self.EXTENSION_DOCX = '.docx'
        self.EXTENSION_EXEL = '.exel'

    def create_psychological_evaluation_docx(self, form: dict) -> str:
        """Создание документа психологической оценки ребенка"""
        document_descriptor = DocumentManager().create_document(form)
        name_file = self.save_document(document_descriptor, self.EXTENSION_DOCX)
        return name_file

    def save_document(self, descriptor: DocumentDescriptor, extension: str) -> str:
        name_file = descriptor.document_name + extension
        path_to_file = self.path_to_save + name_file
        descriptor.document.save(path_to_file)
        return name_file
