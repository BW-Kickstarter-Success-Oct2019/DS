from flask import Flask, json, jsonify, request, send_file
from io import BytesIO
import requests
import pickle

#testing block
#import json

import numpy as np
import pandas as pd
import sklearn

# specify MODEL_FILE to be loaded
MODEL_FILE = "20191022_logreg_68.sav"

app = Flask(__name__)
# load the model as global
model = pickle.load(open(MODEL_FILE, 'rb'))


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/predict', methods=['POST'])#'GET', 'POST'])
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
        X_pred = pd.DataFrame.from_records(input_json, index=[0])
    except:
        return app.response_class(response=json.dumps({}),
                                  status=400,
                                  mimetype='application/json')


    # 20191021_logreg_68 model only uses goal, duration, country, and category
    # for prediction.
    cols_pred = ['goal', 'duration', 'country', 'category']
    X_pred = X_pred[cols_pred]
    y_pred = model.predict(X_pred.to_numpy())

    #Testing block
    #print(f'prediction is {y_pred}')
    #return None
    return jsonify({'pred': float(y_pred)})


def main():
    # Testing Block
    #test1 = '''{"name": "asdfasdfasdf", "blurb": "asdfasdfasdfadsdfasdfadfasdf", "goal": 800.0, "country": "US", "duration":15.0, "category": "fashion"}'''

    #predict(test1)
    app.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == '__main__':
    main()
