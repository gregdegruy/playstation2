<p align="center"><img src="img/made.png" height="256" width="256"></p>

[![Build Status](https://travis-ci.org/gregdegruy/playstation2.svg?branch=master)](https://travis-ci.org/gregdegruy/playstation2)

Video Game Preservation of the PlayStation 2.

A helper for the [hdl_dump cli](http://web.archive.org/web/20120720230755/http://openps2loader.info/hdldump/howto.html). `hdl_dump` must installed first and `hdlPath` msut point directly to the `hdl_dump.exe`. You'll need [anytoiso](https://www.crystalidea.com/anytoiso/command-line) to support `.bin` conversions. Optionally you can add both `anytoiso` and `hdl_dump` to your environment variables on Windows to remove the need for adding a full paths.

## Setup

Before installing a ton of games with `bulkInjectDvd`, run off the test folder using the full path to the test folder as your `isoDirectoryPath` with a fake `hdd` name to see if the LOGs are generated correctly. Next provide a real `hdd` name (you can get the name of it using hdl_dumb) and add a path to a small list of real games for the `isoDirectoryPath` that follows the same directory structure outlined in the test folder.

When ready provide the full path to your game library uncomment the `subprocess.call(command)` and start loading your games! A 2TB drive can hold about 700 and takes hours to complete.

Currently to delete a game this must be done directly from the PS2.

## Status

Runs on Win10 with Python `3.5.2` on a Seagate FireCuda 2TB SSD ST2000LX001. Report an Issue if it doesn't work on you machine.

Unit test ran against Win10 with Python `3.5.2` and the Linux subsystem on Win10 with Python `2.7.12`.

## Run

Open a terminal as an admin.

Setup python3 virtual env or source it if one already exists.
```python
sudo apt-get update
pip install virtualenv
python3 -m venv env
source env/bin/activate
```

Pull dependencies, replace the HDL variables in main, and run.
```bash
pip install -r requirements.txt
python __main__.py
```
