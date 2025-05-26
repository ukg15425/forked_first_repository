# MY API

## Step By Step

### Create git

### Create Environment

To create an env and install required packeges:

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

### Testing fastAPI endpoint from CLI
```bash
# copy the current url from output
curl http://127.0.0.1:8000 
```

### Testing fastAPI endpoint from BROWSER

Click ctrl + url, after that add /docs subsequently the url to open the swagger interface