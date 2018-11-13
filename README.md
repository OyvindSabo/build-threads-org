## Getting started

### Start the server

```
$env:FLASK_APP = "home.py"
flask run
```

### Start the server in debug mode
```
$env:FLASK_DEBUG = 1
$ flask run
```

### Make server publicly available
```
flask run --host=0.0.0.0
```