import json
import pickle
import numpy as np

__model = None

def load_saved_artifacts():
    print('loading saved artifacts......... start')
    global __model
    with open("./artifacts/student_anxiety_level_model.pickle", 'rb') as f:
        __model = pickle.load(f)

    print('loading saved artifacts......... done')

def predict_stress(feature_set):
    feature_set = np.array(feature_set).reshape(1, -1)
    y_pred = __model.predict(feature_set)
    return y_pred

if __name__ == "__main__":
    load_saved_artifacts()
    #features1 = [20, 0, 11, 2, 1, 2, 4, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 1]
    #print(predict_stress(features1))

