from flask import Flask, request, jsonify
app = Flask('muricanize')
import argparse

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from muricanize.lib.translate import Translator

parser = argparse.ArgumentParser()
parser.add_argument('--debug', action='store_true', help='Runs the application in debug mode.')
parser.add_argument('--port', type=int, nargs='?', default='32773')

translator = Translator()

@app.route('/')
def hello():
    return 'Hi, I\'m \'Muricanize, here to make your Arabic text to English!\n'

@app.route('/translate', methods=['POST'])
def translate():
    return jsonify(translator.translate(request.form['text']))


if __name__ == '__main__':
    args = parser.parse_args()
    if args.debug:
        app.debug = True
    print('Running on port:', args.port)
    app.run(threaded=True, port=args.port, host='0.0.0.0')
