## Setup
Supporting Video Game Preservation of the PS2. This is a python helper for the hdl_dump cli. [CLI Docs](http://web.archive.org/web/20120720230755/http://openps2loader.info/hdldump/howto.html).
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

# Status

Tested on Win10 with Python `3.5.2`.

| API | Status |
|---|---|
| exe `inject_dvd` -> py `bulkInjectDvd` |✔|
| exe `hdl_toc` -> py `saveGamesListToFile`  |✔|