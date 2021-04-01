PS Eye Virtualcam
===


Run PS Eye Camera on macOs!


### Development

Init submodule:
```bash
$ git submodule init
```

Create virtual env:
```bash
$ python3 -m venv .venv
$ source ./.venv/bin/activate
```

Install requirements:
```bash
$ pip install -r requirements.txt
$ pip install ./pseyepy
```

Run code:

```bash
$ python eye.py
```

Package:

```bash
$ python -m nuitka eye.py
```