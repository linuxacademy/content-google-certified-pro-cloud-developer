from flask import Flask, render_template
from random import random
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

try:
  import googleclouddebugger
  googleclouddebugger.enable(
    breakpoint_enable_canary=True
  )
except ImportError:
  pass


@app.route('/')
def index():
    # only set value of sample_text 70% of the time
    random_value = random()
    if random_value < 0.7:
        sample_text = "This app was written in Python 3. It will fail some of the time."
    return render_template('index.html', sample_text=sample_text)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

