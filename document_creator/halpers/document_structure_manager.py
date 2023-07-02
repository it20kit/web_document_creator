class DocumentStructureManager:
    """Знает структуру шаблона документа и может возвращать нужный элемент документа из шаблона"""

    @staticmethod
    def get_description_document(template: dict) -> dict:
        return template.get('description')

    def get_document_name(self, template: dict) -> str:
        return self.get_description_document(template).get('document_name')

    def get_standard_styles_for_document(self, template: dict) -> dict:
        return self.get_description_document(template).get('standard_styles_for_document')

    @staticmethod
    def get_margins_sizes_from_standard_style(standard_style: dict) -> dict:
        return standard_style.get('margins_sizes')

    @staticmethod
    def get_style_from_standard_style(standard_style: dict) -> dict:
        return standard_style.get('style')

    @staticmethod
    def get_document_from_template(template) -> dict:
        return template.get('document')

    def get_block_from_template(self, template: dict) -> list:
        return self.get_document_from_template(template).get('blocks')

    @staticmethod
    def get_title_block_from_block(block: dict) -> dict:
        return block.get('title')

    @staticmethod
    def get_parameters_block_from_block(block: dict) -> dict:
        return block.get('parameters')

    def get_style_from_block(self, block: dict) -> list:
        return self.get_parameters_block_from_block(block).get('style')

    def get_table_size_from_block(self, block: dict) -> list:
        return self.get_parameters_block_from_block(block).get('table_size')

    @staticmethod
    def get_type_of_block_handler(block: dict) -> str:
        return block.get('type_of_block_handler')

    @staticmethod
    def get_subblock_from_block(block: dict) -> list:
        return block.get('subbblocks')

    @staticmethod
    def get_style_document_from_description(description: dict) -> dict:
        return description.get('style')

    def get_classes_style_from_style(self, description) -> dict:
        return self.get_style_document_from_description(description).get('classes')

    def get_content_from_block(self, block: dict) -> list:
        return block.get('content')

    @staticmethod
    def get_value_from_content(content: dict) -> list:
        return content.get('value')

    @staticmethod
    def get_value_by_heading(block: dict):
        return block.get('content').get('value')

    def get_type_block_from_block(self, block):
        return self.get_parameters_block_from_block(block).get('type_block')
