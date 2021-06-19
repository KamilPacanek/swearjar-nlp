if [ ! -f pl_core_news_sm-3.0.0.tar.gz ]; then
    wget https://github.com/explosion/spacy-models/releases/download/pl_core_news_sm-3.0.0/pl_core_news_sm-3.0.0.tar.gz
fi

tar -xf pl_core_news_sm-3.0.0.tar.gz

mkdir pl_core_news_sm
mv pl_core_news_sm-3.0.0/pl_core_news_sm/pl_core_news_sm-3.0.0/* pl_core_news_sm

rm -rf pl_core_news_sm-3.0.0
rm pl_core_news_sm-3.0.0.tar.gz
