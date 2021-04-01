PS Eye Virtualcam
===


Run PS Eye Camera on macOs!

### Usage

- Download latest executable from [releases](https://github.com/dbtek/pseye-virtualcam/releases)
- Install [OBS](https://obsproject.com/tr)
- In OBS:
  - Start virtual cam
  - Stop virtual cam
- Start pseyevcam
- Enjoy

### Development

Init submodule:
```bash
$ git submodule init
$ git submodule update
```

Create virtual env:
```bash
$ python3 -m venv .venv
$ source ./.venv/bin/activate
```

Install requirements:
```bash
$ pip install -r requirements.txt
$ sudo -H pip install ./pseyepy
```

Run code:

```bash
$ python eye.py
```

Package:

```bash
$ python -m nuitka eye.py
```