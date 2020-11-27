from flask import Flask, render_template
from os import environ, path

app = Flask(__name__)

NUM_DOGS = environ.get("NUM_DOGS", default="")
NUM_CATS = environ.get("NUM_CATS", default="")

@app.route('/', methods=['GET'])
def index():

    # default values
    variables = 'Environment variables not set!'
    configfile = 'Config file not found!'

    # attempt to read environment variables
    if NUM_DOGS != "" and NUM_CATS != "":
        variables = "Number of dogs: %s\nNumber of cats: %s" % (NUM_DOGS, NUM_CATS)

    # attempt to read local config file
    if path.isfile('/data/animals.cfg'):
        f = open('/data/animals.cfg', 'r')
        configfile = f.read()
        f.close()

    return render_template('index.html', variables=variables,
                           configfile=configfile)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)

