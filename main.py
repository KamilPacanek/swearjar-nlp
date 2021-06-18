from flask import Flask
from flask import request, escape

#import en_core_web_trf
import pl_core_news_lg


app = Flask(__name__)
#nlp_en = en_core_web_trf.load()
#nlp = {"en" : nlp_en, "pl":nlp_pl}
nlp_pl = pl_core_news_lg.load()
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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
