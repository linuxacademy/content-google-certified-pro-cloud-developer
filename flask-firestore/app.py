from flask import Flask, render_template, url_for, request, redirect
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client()


@app.route('/', methods=['post', 'get'])
def index():

    # if 'GET' then display the index page
    if request.method == 'GET':
        # retrieve documents from collection in firestore
        db_ref = db.collection(u'compscientists')
        docs = db_ref.stream()

        # convert documents to python dicts for ease of use
        scientists = []
        for doc in docs:
            scientist = doc.to_dict()
            scientists.append(scientist)

        # render the template
        return render_template('index.html', docs=scientists)

    # if 'POST' then update the db and redirect
    if request.method == 'POST':
        # get the values from the form
        first = request.form.get('first')
        last = request.form.get('last')
        birthyear = int(request.form.get('birthyear')) # convert string to number

        # get a reference to the collection in firestore
        db_ref = db.collection(u'compscientists')
        # add a new document
        db_ref.add({u'first': first, u'last': last, u'birthyear': birthyear})

        # redirect to the index page
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
