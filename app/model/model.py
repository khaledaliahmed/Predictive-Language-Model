import pickle
import re 
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained_pipeline.pkl", "rb") as f:
    model = pickle.load(f)



classes = ['Arabic', 'Danish', 'Dutch', 'English', 'French', 'German',
       'Greek', 'Hindi', 'Italian', 'Kannada', 'Malayalam', 'Portugeese',
       'Russian', 'Spanish', 'Sweedish', 'Tamil', 'Turkish']



def predict_pipline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    text = text.lower()
    pred = model.pradict([text])
    return classes[pred[0]]