from document_factory.document_block_handlers.text_creator import TextCreator
from document_factory.document_block_handlers.paragraph_creator import ParagraphCreator


class TableCreator:
    """Умеет создавать различные таблицы"""

    @staticmethod
    def create_empty_table_by_parameters(document, rows: int, cols: int):
        """Создает пустую таблицу по числу строк и столбцов"""
        table = document.add_table(rows=rows, cols=cols)
        table.style = 'Table Grid'
        table.width = 1
        return table

    def create_table_with_two_columns_by_text_style(
            self, document, data: dict, style_one: dict = None, style_two: dict = None
    ):
        table = self.create_empty_table_by_parameters(document=document, rows=7, cols=2)
        for i in range(len(data)):
            translation = data[i].get('translation')
            value = data[i].get('value')
            cell = table.cell(i, 0)
            self.__add_content_for_cell_table(cell, translation, style_one)
            if value is not None:
                cell = table.cell(i, 1)
                self.__add_content_for_cell_table(cell, value, style_two)

    def create_table_two_columns(self, document, data):
        style_for_first_column = data.get('style').get('style_for_first_column')
        style_for_second_column = data.get('style').get('style_for_second_column')
        self.create_table_with_two_columns_by_text_style(
            document,
            data.get('content'),
            style_for_first_column,
            style_for_second_column
        )

    @staticmethod
    def __add_content_for_cell_table(cell, content, style: dict) -> None:
        """Добавить текст в ячейку таблицы с переданными параметрами"""
        text = cell.paragraphs[0].add_run(content)
        ParagraphCreator().set_style_for_paragraph(cell.paragraphs[0], style)
        TextCreator().set_text_style_by_parameters(text, style)
