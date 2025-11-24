import os
from src.data_loader import load_data
from src.analyzer import compute_metrics
from src.visualizer import plot_subject_average, plot_student_percentages

def main():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'students.csv')
    data_path = os.path.abspath(data_path)
    df = load_data(data_path)
    if df is None:
        print('Failed to load data. Exiting.')
        return

    df, class_avg, subject_avg, toppers = compute_metrics(df)

    print('--- Class Summary ---')
    print(f'Class Average Percentage: {class_avg:.2f}%')
    print('\n--- Subject Averages ---')
    print(subject_avg.to_string())

    print('\n--- Subject Toppers ---')
    for s, info in toppers.items():
        print(f'{s}: Roll {info["roll"]} with {info["marks"]} marks')

    # create visualizations
    out1 = plot_subject_average(subject_avg)
    out2 = plot_student_percentages(df)
    print(f'Generated plots: {out1}, {out2}')
    # Save cleaned & enriched CSV
    out_csv = os.path.join(os.path.dirname(__file__), '..', 'reports', 'enriched_students.csv')
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    df.to_csv(out_csv, index=False)
    print(f'Enriched CSV saved: {out_csv}')

if __name__ == '__main__':
    main()
