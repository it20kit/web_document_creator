from fastapi import FastAPI
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from forms.form_descriptor import FormDescriptor
from i_document.i_document import IDocument
from i_document.document_manager import DocumentManager

app = FastAPI()
app.mount('/upload', StaticFiles(directory='dist'), name='upload')


@app.get('/')
async def homepage():
    """Контролер домашней страницы"""
    return JSONResponse({"name": "Konstantin"})

@app.post('/api/psychological_evaluation')
async def create_psychological_evaluation_docx(form_descriptor: FormDescriptor):
    """Контролер для создания психологической оценки ребенка"""
    path_to_file = IDocument().create_psychological_evaluation_docx(form_descriptor.field)
    return JSONResponse({'url':  path_to_file})
