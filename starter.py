#!/usr/bin/python

from flask import Flask, request, jsonify
from flask import render_template
from sentimental_analysis import Corpus
from sentimental_analysis import Classifier

app = Flask(__name__)


# @app.route("/co", methods=['GET', 'POST'])
# def co():
#     if request.method == 'POST':
        # positive_training_data_path = './data/positive_x'
        # negative_training_data_path = './data/negative_x'
        # positive_corpus = Corpus()
        # negative_corpus = Corpus()
        # positive_corpus.load_from_directory(positive_training_data_path)
        # negative_corpus.load_from_directory(negative_training_data_path)
        # classifier = Classifier(positive_corpus, negative_corpus)
        # classifying_output = classifier.classify(request.form['nicedit-message'])
        # print request.form
        # return 'a'
        # return jsonify(prob=classifying_output['probability'], sentiment=classifying_output['sentiment'], )


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        positive_training_data_path = './data/positive_x'
        negative_training_data_path = './data/negative_x'

        positive_corpus = Corpus()
        negative_corpus = Corpus()

        positive_corpus.load_from_directory(positive_training_data_path)
        negative_corpus.load_from_directory(negative_training_data_path)

        classifier = Classifier(positive_corpus, negative_corpus)
        classifying_output = classifier.classify(request.form['nicedit-message'])
        return render_template('index.html', co=classifying_output)
        
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run()