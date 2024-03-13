## Delta sharing demo

Welcome to the Delta Sharing demo. This demo shows how to use as a client Delta Sharing to download tables as CSV files. To download the data from a python script run technical_user.py. For downloading the data with a UI, run business_user.py

## Install

```
python3 -m venv venv
brew install python-tk
source activate venv/bin/activate
pip install delta-sharing tkinter
```

## Run the code
First download your delta share file into data/config.share

Then run
```
python3 technical_user.py
```
or
```
python3 business_user.py
```

When the window pops up, click on download. Your table will be donwloaded to the downloads folder