## Getting started

### Start the server

```
$env:FLASK_APP = "home.py"
flask run
```

### Turn on debug mode
```
$env:FLASK_DEBUG = 1
```

### Turn off debug mode
```
$env:FLASK_DEBUG = 0
```

### Make server publicly available
```
flask run --host=0.0.0.0
```