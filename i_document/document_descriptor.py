from docx import Document


class DocumentDescriptor:
    """Дескриптор документа, содержащий имя и сам документ"""

    def __init__(self, name: str, document: Document):
        self.__document_name = name
        self.__document = document

    @property
    def document(self) -> Document:
        return self.__document

    @document.setter
    def document(self, document: Document()):
        self.__document = document

    @property
    def document_name(self) -> str:
        return self.__document_name

    @document_name.setter
    def document_name(self, name: str):
        self.__document_name = name
