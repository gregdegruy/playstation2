<p align="center"><img src="img/made.png" height="256" width="256"></p>

Supporting Video Game Preservation of the PS2.

This is a python helper for the hdl_dump cli. [Docs](http://web.archive.org/web/20120720230755/http://openps2loader.info/hdldump/howto.html). You'll need the hdl_dump cli installed to run this and `hdlPath` point directly to the `hdl_dump.exe` file. You'll need [anytoiso](https://www.crystalidea.com/anytoiso/command-line) to handle `.bin` conversions.

## Setup

Before installing a ton of games with `bulkInjectDvd`, run off the test folder using the full path to the test folder as your `isoDirectoryPath` with a fake `hdd` name to see if the LOGs are generated correctly. Next provide a real `hdd` name (you can get the name of it using hdl_dumb) and add a path to a small list of real games for the `isoDirectoryPath` that follows the same directory structure outlined in the test folder.

Once you're ready provide the full path to your game library uncomment the `procOutput = subprocess.getoutput(command)` and start loading your games! Testing on a 2TB drive has shown about 700 games can fit no problem and takes hours to complete.

Currently to delete a game this must be done directly from the PS2.

## Run

Setup python3 virtual env or source it if one already exists.
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

Tested on Win10 with Python `3.5.2` on a Seagate FireCuda 2TB SSD ST2000LX001. Report an Issue to raise a bug.

| API | Status |
|---|---|
| exe `inject_dvd` -> py `bulkInjectDvd` |✔|
| exe `hdl_toc` -> py `saveGamesListToFile`  |✔|