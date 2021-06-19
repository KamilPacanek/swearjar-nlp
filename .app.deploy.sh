if [ ! -f pub/pipelines ]; then
    mkdir pub/pipelines
fi
cp -r app.yaml app.py .app.* pub/
cp -r pipelines/init.sh pub/pipelines
source env/deploy.remote.sh
