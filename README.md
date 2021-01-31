# Read File

Setup:

```
cd myproject
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Compile:

```
pyinstaller --name="Read-File" --onefile read_file.py
```