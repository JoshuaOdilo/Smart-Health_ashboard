
from sklearn.linear_model import LogisticRegression
import pandas as pd

class HealthPredictor:
    def __init__(self):
        self.model = LogisticRegression(max_iter=1000)
        self.trained = False

    def train(self, df: pd.DataFrame):
        features = df[['age', 'heart_rate', 'blood_pressure', 'cholesterol']]
        target = df['outcome'].apply(lambda x: 1 if x == 'At Risk' else 0)
        self.model.fit(features, target)
        self.trained = True
        return self.model.score(features, target)

    def predict(self, input_data: dict) -> str:
        if not self.trained:
            raise Exception("Model not trained")
        input_df = pd.DataFrame([input_data])
        prediction = self.model.predict(input_df)[0]
        return "At Risk" if prediction == 1 else "Healthy"
