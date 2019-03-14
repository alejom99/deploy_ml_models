import json
import threading
import pickle
import pandas as pd

clf = pickle.load(open("model.p", "rb"))

def titanic_predict(event, context):
    sample = event.get('sample')
    print(sample)
    test = pd.DataFrame.from_dict(sample)
    result = clf.predict(test)
    return result.tolist()

