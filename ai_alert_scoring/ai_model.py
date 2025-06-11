
# ai_model.py
        import joblib
        import numpy as np

        def load_model(path='model.pkl'):
            return joblib.load(path)

        def predict_threat(features, model):
            return model.predict([features])[0]
