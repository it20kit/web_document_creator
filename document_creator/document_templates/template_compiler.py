import re
import json
from document_creator.halpers.document_structure_manager import DocumentStructureManager


class TemplateCompiler:
    """Создает шаблон документа по заполненной форме"""

    def __init__(self):
        self.document_structure_manager = DocumentStructureManager()

    def compile_template(self, path_to_template: str, form: object) -> dict:
        """Заполнить шаблон документа данными из формы"""
        form = self.make_dictionary_out_of_form(form)
        with open(path_to_template, 'r') as file:
            json_str = file.read()
            for key, value in form.items():
                pattern = "{{" + key + "}}"
                if value is not None:
                    json_str = re.sub(pattern, value, json_str)
            compiled_template = json.loads(json_str)

            return compiled_template

    @staticmethod
    def make_dictionary_out_of_form(form: object):
        """Сделать из объекта словарь"""
        return vars(form)

    def create_form_by_template(self, path_to_template: str):
        form = {}
        block = {}
        form['blocks'] = []
        template = self.__get_json_str_from_template(path_to_template)
        blocks_document = self.document_structure_manager.get_block_from_template(template)
        for blocks in blocks_document:
            if blocks.get('changeable_block'):
                block_title = self.document_structure_manager.get_title_block_from_block(blocks)
                subblock = self.document_structure_manager.get_subblock_from_block(blocks)
                if block_title is not None:
                    text_title = self.__get_text_from_block_title(block_title)
                    block['title'] = text_title
                if subblock is not None:
                    content_subblock = self.__get_content_subblok(subblock)
                    block['subblock'] = content_subblock
                form['blocks'].append(block)
                block = {}
        return form

    def __get_text_from_block_title(self, block_title: dict):
        text_title = ""
        content_block = self.document_structure_manager.get_value_by_heading(block_title)
        for text in content_block:
            text_title += text
        return text_title

    def __get_content_subblok(self, subblock: list) -> list:
        content_subblock = []
        box = {}
        for block in subblock:
            type_block = self.document_structure_manager.get_type_block_from_block(block)
            box['tipe_block'] = type_block
            cells_block = self.document_structure_manager.get_content_from_block(block)
            content_cell_block = self.__get_content_cell_block(cells_block)
            box['content'] = content_cell_block
            content_subblock.append(box)
        return content_subblock

    def __get_content_cell_block(self, cells: list) -> list:
        content_cell_block = []
        box = {}
        for cell in cells:
            value_cell = cell.get('value')
            title = value_cell[0]
            key = self.__validate_string(value_cell[1])
            box['title'] = title
            box['key'] = key
            box['choosing_multiple_options'] = cell.get('choosing_multiple_options')
            box['can_disable'] = cell.get('can_disable')
            box['add_option'] = cell.get('add_option')
            box['default'] = cell.get('default')
            content_cell_block.append(box)
            box = {}
        return content_cell_block

    @staticmethod
    def __validate_string(string: str) -> str:
        return string.strip("{}")

    @staticmethod
    def __get_json_str_from_template(path_to_template) -> dict:
        with open(path_to_template, 'r') as file:
            json_str = file.read()
        return json.loads(json_str)
