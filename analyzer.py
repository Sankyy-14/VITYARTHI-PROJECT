import pandas as pd

def compute_metrics(df):
    # Assumes first column is ID and remaining are subject marks
    subjects = list(df.columns[1:])
    df['Total'] = df[subjects].sum(axis=1)
    # Percentage assuming each subject max marks = 100
    df['Percentage'] = df['Total'] / (len(subjects) * 100) * 100
    def grade(p):
        if p >= 90: return 'A'
        if p >= 75: return 'B'
        if p >= 60: return 'C'
        return 'D'
    df['Grade'] = df['Percentage'].apply(grade)

    class_avg = df['Percentage'].mean()
    subject_avg = df[subjects].mean()

    # subject toppers
    toppers = {}
    for s in subjects:
        idx = df[s].idxmax()
        toppers[s] = { 'roll': int(df.loc[idx, df.columns[0]]), 'marks': float(df.loc[idx, s]) }

    return df, class_avg, subject_avg, toppers
