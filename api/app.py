from flask import Flask, json, jsonify, request, send_file
from io import BytesIO
import requests
import pickle

import nltk
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize

import numpy as np
import pandas as pd
import sklearn

# specify MODEL_FILE to be loaded
nltk.download('punkt')
MODEL_FILE = "20191023_logreg_text_69.sav"
CT_FILENAME = "20191023_preproc.sav"
D2V_FILENAME = "d2v.model"

# load the model as global
model = pickle.load(open(MODEL_FILE, 'rb'))
ct_model = pickle.load(open(CT_FILENAME, 'rb'))
d2v = Doc2Vec.load(D2V_FILENAME)
app = Flask(__name__)
print("model_loaded")

@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/predict', methods=['POST'])
def predict():
    """
    Parameters:
    ===========
    Expectd JSON POST format:
    {'name': string,
     'blurb': string,
     'goal': float,
     'country': string(2),
     'duration': float,
     'category': string,
    }

    Returns:
    ========
    Model predictions in json. Return format:
    {'pred': float}
    """
    # get input JSON from POST
    input_json = request.get_json(force=True)
    #input_json = json.loads(input_json)
    print(input_json)

    # parse POST input JSON w/ error checking
    try:
        #
        # TODO: Add type checkingtype checking
#         name = input_json['name']
#         blurb = input_json['blurb']
#         goal = input_json['goal']
#         country = input_json['country']
#         duration = input_json['duration']
#         category = input_json['category']
        X_pred = pd.DataFrame.from_records(input_json, index=[0], columns=['name', 'blurb', 'goal', 'country', 'duration', 'category'])
    except:
        return app.response_class(response=json.dumps({}),
                                  status=400,
                                  mimetype='application/json')
    
    # Preprocessing
    X_no_text = ct_model.transform(X_pred).toarray()
    n = d2v.infer_vector(word_tokenize(X_pred.name[0].lower())).reshape(-1, 10)
    b = d2v.infer_vector(word_tokenize(X_pred.blurb[0].lower())).reshape(-1, 10)
    X_inference = np.hstack([n, b, X_no_text])
    
    # Prediction
    y_pred = model.predict_proba(X_inference)[:, 1]

    return jsonify({'pred': float(y_pred)})


def main():
    
    app.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == '__main__':
    main()
