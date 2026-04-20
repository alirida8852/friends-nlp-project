
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import sys
import os

# allow importing from src/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.translator import friends_translator
from src.catchphrase import detect_catchphrase   # <-- NEW

# initialize app
app = FastAPI()

# CORS (for frontend)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# request format
class InputText(BaseModel):
    text: str

# load model + vectorizer (SAFE PATH)
with open(os.path.join(BASE_DIR, "models", "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, "models", "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)


# health check
@app.get("/")
def home():
    return {"message": "Friends NLP API is running!"}


# main prediction route
@app.post("/predict")
def predict(data: InputText):
    try:
        text = data.text.strip()

        # 🟢 STEP 1: Catchphrase detection (priority)
        character, phrase = detect_catchphrase(text)

        if character:
            pred = character
            source = "catchphrase"
        else:
            # 🟢 STEP 2: ML prediction
            pred = model.predict(vectorizer.transform([text]))[0]
            source = "model"

        # 🟢 STEP 3: Style translation
        output = friends_translator(text, pred)

        return {
            "input": text,
            "predicted_character": pred,
            "response": output,
            "source": source   # tells how it was predicted
        }

    except Exception as e:
        return {
            "error": str(e)
        }