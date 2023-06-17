from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from document_factory.document_factory import IDocument
from forms.form_for_psychological_evaluation import FormForPsychologicalEvaluation
from document_factory.templates.template_compiler import TemplateCompiler

app = FastAPI()
app.mount('/upload', StaticFiles(directory='dist'), name='upload')


@app.get('/')
async def homepage():
    """Контролер домашней страницы"""
    return JSONResponse({"name": "Konstantin"})


@app.post('/psychological_evaluation')
async def create_psychological_evaluation_docx(form: FormForPsychologicalEvaluation):
    """Контролер для создания психологической оценки ребенка"""
    path_to_template = 'document_factory/templates/psychological_evaluation_form.json'
    completed_template = TemplateCompiler().compile_template(path_to_template, form)
    path_to_file = IDocument('./dist/').create_psychological_evaluation_docx(completed_template)
    return JSONResponse({'url': '/upload/' + path_to_file})
    # TemplateCompiler().test(completed_template)
    # return completed_template
