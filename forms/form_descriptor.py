from forms.form_for_psychological_evaluation import FormForPsychologicalEvaluation
from pydantic import BaseModel


class FormDescriptor(BaseModel):
    """Дескриптор формы который содержит заголовок и поля для создания документа"""
    title: str
    field: FormForPsychologicalEvaluation
