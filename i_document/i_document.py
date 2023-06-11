from i_document.document_manager import DocumentManager
from i_document.creators.psychological_evaluation_creator_docx import PsychologicalEvaluationCreatorDocx


class IDocument:
    """Библиотека умеющая создавать нужные документы"""

    def __init__(self):
        pass

    @staticmethod
    def create_psychological_evaluation_docx(form: object):
        """Создание документа психологической оценки ребенка"""
        return DocumentManager('./dist/').create_document(PsychologicalEvaluationCreatorDocx(),form)
