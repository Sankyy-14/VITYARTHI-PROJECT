import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(path)
        # Basic validation: expect first column to be identifier and rest numeric marks
        if df.shape[1] < 2:
            raise ValueError("CSV must contain at least 2 columns: ID and one subject.")
        df = df.fillna(0)
        # ensure numeric for marks
        for c in df.columns[1:]:
            df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0)
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None
