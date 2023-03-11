import openai
from fastapi import FastAPI, File, UploadFile
from PyPDF2 import Pdfreader

app = FastAPI()

@app.post("/api/doc")
async def get_summary(file: UploadFile = File()):
    reader = Pdfreader(file.file)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    
    # extract text from the pdf, pass to an openai prompt, and return the text summarization for now