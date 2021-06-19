pip install -U pip setuptools wheel
pip install -U spacy

if [ ! -f explacy.py ]; then
    wget https://raw.githubusercontent.com/tylerneylon/explacy/master/explacy.py
fi

python3 -m venv .dev
source .dev/bin/activate

pip install flask pandas sklearn
