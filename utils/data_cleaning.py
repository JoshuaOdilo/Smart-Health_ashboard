
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.dropna(subset=['age', 'heart_rate', 'blood_pressure', 'cholesterol', 'outcome'])
    df['age'] = df['age'].astype(int)
    df['heart_rate'] = df['heart_rate'].astype(int)
    df['blood_pressure'] = df['blood_pressure'].astype(int)
    df['cholesterol'] = df['cholesterol'].astype(int)
    return df
