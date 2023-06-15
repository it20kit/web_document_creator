from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from document_factory.i_document import IDocument
from forms.form_for_psychological_evaluation import FormForPsychologicalEvaluation
from templates.template_compiler import TemplateCompiler

app = FastAPI()
app.mount('/upload', StaticFiles(directory='dist'), name='upload')


@app.get('/')
async def homepage():
    """Контролер домашней страницы"""
    return JSONResponse({"name": "Konstantin"})


@app.post('/psychological_evaluation')
async def create_psychological_evaluation_docx(form: FormForPsychologicalEvaluation):
    """Контролер для создания психологической оценки ребенка"""
    path_to_template = './templates/test.json'
    completed_template = TemplateCompiler().compile_template(path_to_template, form)
    path_to_file = IDocument('./dist/').create_psychological_evaluation_docx(completed_template)
    return JSONResponse({'url':  path_to_file})
