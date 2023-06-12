import datetime
from langdetect import detect
from transliterate import translit


class DocumentNameFactory:
    """Умеет создавать имена для документов"""

    def __init__(self, expansion):
        self.expansion = expansion
        self.unwanted_symbol = ('ь', 'ъ', '\'', '/', '\\')

    def create_name_for_document(self, name: str) -> str:
        """Создать имя документа"""
        today_data = str(datetime.date.today())
        valid_name = self.validate_name(name)
        return valid_name + '_' + today_data + self.expansion

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
