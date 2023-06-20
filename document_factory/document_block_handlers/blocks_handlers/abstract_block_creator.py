from abc import ABC, abstractmethod
import re
from docx import Document


class AbstractBlockCreator(ABC):
    """Описывает структуру конструкторов блоков и содержит общие методы конструкторов"""

    @abstractmethod
    def create_block(self, document: Document, data: dict) -> None:
        pass

    @staticmethod
    def is_value_empty(value: str) -> bool:
        return re.match('{{.+}}', value) is not None

    @staticmethod
    def get_style(data: dict) -> dict | bool:
        parameters = data.get('parameters')
        if parameters is not None:
            style = parameters.get('style')
            if style is not None:
                return style
        return False

    def are_there_empty_values_in_content(self, content: list) -> bool:
        for i in range(len(content)):
            if self.is_value_empty(content[i]):
                return True
        return False
