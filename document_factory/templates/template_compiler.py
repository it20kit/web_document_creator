import re
import json


class TemplateCompiler:
    """Создает шаблон документа по заполненной форме"""

    def compile_template(self, path_to_template: str, form: object):
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
        return vars(form)

    def test(self, form):
        for key, value in form.items():
            print(type(value))

