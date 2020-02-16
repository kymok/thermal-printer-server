from flask import Flask, request
from flask_cors import CORS
from thermalprinter import ThermalPrinter

import logging
#import auxiliary_module

# logger
logger = logging.getLogger('keyswitch_tester')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('../thermal_printer.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s, %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# params
printer_port='/dev/tty.usbserial-A601E88T'
baudrate=9600
flask_host='0.0.0.0'
flask_port=5000
doLogging=True

# start printer
#TODO error if cannot connect to the printer
printer = ThermalPrinter(port=printer_port, baudrate=baudrate)

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return ''

#TODO 400 BAD REQUEST if print parameter error
@app.route('/thermal-printer/v1/print', methods=['POST'])
def thermal_print():
    content = request.json
    lines = content.get('lines', [])
    for line in lines:
        text = line.get('text', '')
        bold = line.get('bold', False)
        char_spacing = line.get('char_spacing', 0)
        double_height = line.get('double_height', False)
        double_width = line.get('double_width', False)
        inverse = line.get('inverse', False)
        justify = line.get('justify', 'L')
        left_margin = line.get('left_margin', 0)
        rotate = line.get('rotate', 0)
        size = line.get('size', 'S')
        strike = line.get('strike', False)
        underline = line.get('underline', False)
        upside_down = line.get('upside_down', False)
        
        if (doLogging):
            logger.info(text)

        printer.out(
            text,
            bold=bold,
            char_spacing=char_spacing,
            double_height=double_height,
            double_width=double_width,
            inverse=inverse,
            justify=justify,
            left_margin=left_margin,
            rotate=rotate,
            size=size,
            strike=strike,
            underline=underline,
            upside_down=upside_down
            )
    print('print done')
    return 'OK'

if __name__ == '__main__':
    app.run(host=flask_host, port=flask_port)
