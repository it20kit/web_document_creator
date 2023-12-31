import datetime
from langdetect import detect
from transliterate import translit
import string
import random
from document_creator.halpers.document_structure_manager import DocumentStructureManager


class DocumentNameManager:
    """Умеет создавать имена для документов"""

    def __init__(self):
        self.unwanted_symbol = ('ь', 'ъ', '\'', '/', '\\', '{', '}', '[', ']')
        self.document_structure_manager = DocumentStructureManager()

    def create_name_for_document(self, data: dict) -> str:
        """Создать имя документа"""
        length = 10
        name = self.document_structure_manager.get_document_name(data)
        if name is None or name == "":
            name = self.generate_document_name(length)
        today_data = str(datetime.date.today())
        valid_name = self.validate_name(name)
        return valid_name + '_' + today_data

    def validate_name(self, name: str) -> str:
        """Валидировать имя, убрать нежелательные символы ь и ъ """
        valid_name = ''
        for litter in name:
            if litter in self.unwanted_symbol:
                continue
            valid_name = valid_name + litter

        if detect(name) == 'ru':
            valid_name = translit(valid_name, "ru", reversed=True)

        valid_name = valid_name.replace(' ', '_')
        return valid_name

    @staticmethod
    def generate_document_name(length: int):
        """Сгенерировать случайное имя документа"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
