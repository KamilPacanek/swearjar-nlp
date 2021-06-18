pip install -U pip setuptools wheel
pip install -U spacy[transformers,lookups]
py -m spacy download en_core_web_trf
py -m spacy download pl_core_news_lg

py -m venv dev

 Set-ExecutionPolicy Bypass Process
.\dev\Scripts\Activate.ps1
 Set-ExecutionPolicy Bypass Undefined

 py -m pip install -r .\requirements.txt
