# Labtrak

Application (Work In Progress)

### Requirements
- [mongoDB](http://www.mongodb.org/)
- [Python 3](https://www.python.org/)
- [pip3](https://pip.pypa.io/en/latest/installing.html)
- [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) (recommended)

### Set up Python environment (install dependencies via pip)
```
$ cd Labtrak
$ virtualenv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

### Run locally
```
$ source venv/bin/activate
$ sudo mongod
$ python3 server.py
 * Running on http://0.0.0.0:5000/
```

### Contributing
Use branching and pull requests!
