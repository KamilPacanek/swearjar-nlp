pip install aicrowd-cli

mkdir data

aicrowd login --api-key $(cat aicrowd.apikey)
aicrowd dataset download --challenge emotion-detection -j 3 -o data
