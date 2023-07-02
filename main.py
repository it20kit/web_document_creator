from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from document_creator.document_creator import DocumentCreator
from forms.form_for_psychological_evaluation import FormForPsychologicalEvaluation
from document_creator.document_templates.template_compiler import TemplateCompiler

app = FastAPI()
app.mount('/upload', StaticFiles(directory='dist'), name='upload')


@app.get('/')
async def homepage():
    """Контролер домашней страницы"""
    return JSONResponse({"name": "Konstantin"})


@app.post('/psychological_evaluation')
async def create_psychological_evaluation_docx(form: FormForPsychologicalEvaluation):
    """Контролер для создания психологической оценки ребенка"""
    path_to_template = 'document_creator/document_templates/psychological_evaluation_form.json'
    completed_template = TemplateCompiler().compile_template(path_to_template, form)
    path_to_file = DocumentCreator('./dist/').create_psychological_evaluation_docx(completed_template)
    return JSONResponse({'url': '/upload/' + path_to_file})


@app.get('/get_psychological_evaluation_form')
async def create_form():
    form = TemplateCompiler().create_form_by_template(
        'document_creator/document_templates/psychological_evaluation_form.json'
    )
    return JSONResponse(form)
