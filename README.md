## Setup
Supporting Video Game Preservation of the PS2. This is a python helper for the hdl_dump cli.
Your iso directory must be at the same level as `__main__.py`. You'll need the hdl_dump cli installed to run this.

## Run

Setup python3 virtual env.
```python
sudo apt-get update
pip install virtualenv
python3 -m venv env
source env/bin/activate
```

Pull depdendencies and run.
```bash
pip install -r requirements.txt
python __main__.py
```
