import threading
import pickle
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model from pickle file
clf = pickle.load(open("model.p", "rb"))

@app.route('/predict', methods=('POST',))
def predict():
    request_data = request.get_json()
    sample = request_data.get('sample')
    test = pd.DataFrame.from_dict(sample)
    result = clf.predict(test)
    
    return jsonify(result.tolist())