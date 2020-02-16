# Thermal Printer Server

## About

This python script turns a Raspberry pi into a thermal printer API server.
The script is a minimal wrapper of [thermalprinter](https://github.com/BoboTiG/thermalprinter) Python library.

The printer can be controlled via JSON POST API as shown below:

```JSON
{
    "lines": [
      {
        "text": "* HELLO *",
        "double_width": true,
        "justify": "C"
      },
      {
        "text": "* WORLD *",
        "double_width": true,
        "justify": "C"
      }
    ]
}
```

![Hello World printed](./doc/img/hello_world.jpg)

## Prerequisites 

### Equipments
- A computer with serial port such as [Raspberry Pi](https://www.raspberrypi.org)
- DP-EH600 thermal printer

### Python
- [thermalprinter](https://github.com/BoboTiG/thermalprinter)
- [Flask](http://flask.palletsprojects.com/en/1.1.x/)
- [Flask-CORS](https://github.com/corydolphin/flask-cors)

## Usage

### Start Server
```
python3 main.py
```

### Sending a request

#### Printing

Send a JSON POST to `/thermal-printer/v1/print/`.

|Name|Type|Default|Remarks|
|:---|:---|:------|:------|
|lines|array|||
|lines: text|string|||
|lines: bold|boolean|false||
|lines: char_spacing|int|0||
|lines: double_height|boolean|false||
|lines: double_width|boolean|false||
|lines: inverse|boolean|false|White on black if true.|
|lines: justify|string|L||
|lines: left_margin|int|0||
|lines: rotate|boolean|false|90 degree rotation.|
|lines: size|int|S|M: double height, L: double height and width.|
|lines: strike|boolean|false||
|lines: underline|boolean|false||
|lines: upside_down|boolean|false||

