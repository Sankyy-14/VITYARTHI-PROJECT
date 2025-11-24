import matplotlib.pyplot as plt
import os

def plot_subject_average(subject_avg, out_dir='reports'):
    os.makedirs(out_dir, exist_ok=True)
    ax = subject_avg.plot(kind='bar', title='Subject-wise Average Marks')
    ax.set_xlabel('Subjects')
    ax.set_ylabel('Average Marks')
    fig = ax.get_figure()
    out_path = os.path.join(out_dir, 'subject_average.png')
    fig.savefig(out_path)
    plt.close(fig)
    return out_path

def plot_student_percentages(df, out_dir='reports'):
    os.makedirs(out_dir, exist_ok=True)
    ax = df.plot(x=df.columns[0], y='Percentage', kind='line', marker='o', title='Student Percentage Trend')
    ax.set_xlabel('Student Roll')
    ax.set_ylabel('Percentage')
    fig = ax.get_figure()
    out_path = os.path.join(out_dir, 'student_percentage_trend.png')
    fig.savefig(out_path)
    plt.close(fig)
    return out_path
