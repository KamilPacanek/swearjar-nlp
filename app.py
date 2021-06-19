from flask import Flask
from flask import request, escape
import spacy

app = Flask(__name__)

nlp_pl = spacy.load("pipelines/pl_core_news_sm")
nlp = { "pl":nlp_pl}

@app.route("/api/ping")
def ping():
    return "Pong!"

@app.route("/api/<string:lang>/analyze", methods = ['POST'])
def analyze(lang):
    try:
        text = request.form["s"]
        doc = nlp[lang](text)
        print([(w.text, w.pos_) for w in doc])
        return ""
    except:
        return ""
