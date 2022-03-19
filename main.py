from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from easynmt import EasyNMT
from typing import List

model = EasyNMT('opus-mt')
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/{text}")
async def translate_get(text):
  return model.translate(text, target_lang='en', source_lang='uk')

@app.post("/")
async def translate_post(request: Request):
    data = await request.json()
    return translate_get(**data)

