from fastapi import FastAPI, HTTPException
from copykitt import generate_branding_snippet, generate_keywords

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


app = FastAPI()

MAX_INPUT_LENGTH = 32

@app.get("/generate_snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet, "keywords": []} 
    
@app.get("/generate_keyword")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": None, "keywords": keywords} 
 

@app.get("/generate_snippet_and_keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}  
 
def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=400, detail=f"Input length too long. Must be under {MAX_INPUT_LENGTH} characters.")
        
# uvicorn copykitt_api:app --reload