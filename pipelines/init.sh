if [ ! -d pl_core_news_sm ]; then
    wget https://github.com/explosion/spacy-models/releases/download/pl_core_news_sm-3.0.0/pl_core_news_sm-3.0.0.tar.gz

    tar -xf pl_core_news_sm-3.0.0.tar.gz

    mkdir pl_core_news_sm
    mv pl_core_news_sm-3.0.0/pl_core_news_sm/pl_core_news_sm-3.0.0/* pl_core_news_sm

    rm -rf pl_core_news_sm-3.0.0
    rm pl_core_news_sm-3.0.0.tar.gz
fi

if [ ! -d en_core_web_sm ]; then
    wget https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz

    tar -xf en_core_web_sm-3.0.0.tar.gz

    mkdir en_core_web_sm
    mv en_core_web_sm-3.0.0/en_core_web_sm/en_core_web_sm-3.0.0/* en_core_web_sm

    rm -rf en_core_web_sm-3.0.0
    rm en_core_web_sm-3.0.0.tar.gz
fi
