import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

SEVERITY_MAP = {0: 'Low', 1: 'Medium', 2: 'High'}

def _generate_synthetic_data(n_samples=200):
    np.random.seed(42)
    severity = np.random.randint(1, 8, n_samples)
    src_ip_len = np.random.randint(7, 15, n_samples)
    dest_ip_len = np.random.randint(7, 15, n_samples)
    is_src_private = np.random.randint(0, 2, n_samples)
    is_dest_private = np.random.randint(0, 2, n_samples)
    alert_count = np.random.poisson(5, n_samples)

    labels = np.where(severity <= 2, 0, np.where(severity <= 5, 1, 2))

    X = np.column_stack([severity, src_ip_len, dest_ip_len, is_src_private, is_dest_private, alert_count])
    return X, labels

def train_model(save_path=MODEL_PATH):
    X, y = _generate_synthetic_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf = RandomForestClassifier(n_estimators=50, random_state=42)
    rf.fit(X_train, y_train)

    lr = LogisticRegression(max_iter=200, random_state=42)
    lr.fit(X_train, y_train)

    model = rf
    joblib.dump(model, save_path)
    return model

def load_model(path=MODEL_PATH):
    if not os.path.exists(path):
        return train_model(path)
    return joblib.load(path)

def predict_threat(features, model):
    pred = model.predict([features])[0]
    return SEVERITY_MAP.get(pred, 'Unknown')

if __name__ == '__main__':
    model = train_model()
    print(f"Model trained and saved to {MODEL_PATH}")
    test_features = [3, 11, 9, 1, 0, 4]
    print(f"Sample prediction: {predict_threat(test_features, model)}")
