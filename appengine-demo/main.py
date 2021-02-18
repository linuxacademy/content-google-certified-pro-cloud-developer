from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    sample_text = "This app was written in Python 3"
    return render_template('index.html', sample_text=sample_text)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

