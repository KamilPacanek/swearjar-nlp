from flask import Flask, request
import spacy, explacy
from joblib import load

app = Flask(__name__)
modelFilename = "training/example.joblib"

#nlp_pl = spacy.load("pipelines/pl_core_news_sm")
nlp_en = spacy.load("pipelines/en_core_web_sm")
nlp = { "en":nlp_en}
clf = load(modelFilename)

@app.route("/api/ping")
def ping():
    return "Pong!"

@app.route("/api/<string:lang>/analyze", methods = ['POST'])
def analyze(lang):
    try:
        text = request.form["s"]
        explacy.print_parse_info(nlp[lang], text)
        x_val = create_data({text}, "en")
        y_val = clf.predict(x_val)
        print(f"Prediction: {y_val}")
        return ""
    except Exception as ex:
        print(ex)
        return ""

def create_data(dataset, lang):
    preprocessed_texts = list(nlp[lang].pipe(dataset))
    return [string.vector for string in preprocessed_texts]
