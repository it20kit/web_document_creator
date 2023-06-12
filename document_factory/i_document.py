from document_factory.document_manager import DocumentManager
from document_factory.creators.psychological_evaluation_creator_docx import PsychologicalEvaluationCreatorDocx
from document_factory.factory.document_name_factory import DocumentNameFactory
from document_factory.document_descriptor import DocumentDescriptor


class IDocument:
    """Библиотека умеющая создавать нужные документы"""

    def __init__(self, path):
        self.path_to_save = path
        self.EXTENSION_DOCX = '.docx'
        self.EXTENSION_EXEL = '.exel'

    def create_psychological_evaluation_docx(self, form: dict):
        """Создание документа психологической оценки ребенка"""
        document_descriptor = DocumentManager().create_document(PsychologicalEvaluationCreatorDocx(), form)
        path_to_file = self.save_document(document_descriptor, self.EXTENSION_DOCX)
        return path_to_file

    def save_document(self, descriptor: DocumentDescriptor, extension: str) -> str:
        name_file = descriptor.document_name
        valid_document_name = DocumentNameFactory(extension).create_name_for_document(name_file)
        path_to_file = self.path_to_save + valid_document_name
        descriptor.document.save(path_to_file)
        return path_to_file
