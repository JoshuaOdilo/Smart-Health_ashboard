
import pandas as pd
from io import BytesIO

def export_csv(df: pd.DataFrame):
    output = BytesIO()
    df.to_csv(output, index=False)
    return output.getvalue()
