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

## Usage

### Start Server
```
python3 main.py
```

### Sending a request

#### Printing

Send a JSON POST to `/thermal-printer/v1/print/`.

|Name|Type|Default|
|:---|:---|:------|
|lines|array||
|lines: text|||
|lines: bold||false|
|lines: char_spacing||0|
|lines: double_height||false|
|lines: double_width||false|
|lines: inverse||false|
|lines: justify||L|
|lines: left_margin||0|
|lines: rotate||false|
|lines: size||S|
|lines: strike||false|
|lines: underline||false|
|lines: upside_down||false|

