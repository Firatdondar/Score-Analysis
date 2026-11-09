from pathlib import Path
import sys
import numpy as np
import pandas as pd


def load_dataset(file_path: Path) -> pd.DataFrame:
    """Load and clean the paired student exam score dataset."""
    if not file_path.exists():
        print(f"[!] ERROR: Dataset file '{file_path}' not found.")
        sys.exit(1)

    data = pd.read_csv(file_path, sep=r'\s+', skipinitialspace=True)
    data.columns = data.columns.str.strip()

    return pd.DataFrame({
        'Math': data['MATEMATIK'].astype(float),
        'Verbal': data['TURKCE'].astype(float),
    })


def analyze_paired_scores(scores: pd.DataFrame) -> None:
    """Compute correlation, paired differences, t-statistic, and Cohen's d effect size."""
    n = len(scores)
    math = scores['Math']
    verbal = scores['Verbal']

    # Correlations
    pearson_r = math.corr(verbal, method='pearson')
    spearman_rho = math.corr(verbal, method='spearman')
    r_squared = pearson_r ** 2

    # Paired differences (Math - Verbal)
    diff = math - verbal
    mean_diff = diff.mean()
    std_diff = diff.std(ddof=1)
    se_diff = std_diff / np.sqrt(n)
    ci_95 = 1.96 * se_diff

    # Paired Student's t-statistic & Cohen's d effect size
    t_stat = mean_diff / se_diff if se_diff > 0 else 0.0
    cohens_d = mean_diff / std_diff if std_diff > 0 else 0.0

    math_higher = int((diff > 0).sum())
    verbal_higher = int((diff < 0).sum())
    tied = int((diff == 0).sum())

    print("=" * 68)
    print("         PAIRED SCORE CORRELATION & DIFFERENCE ANALYSIS")
    print("=" * 68)
    print(f"  Sample Size (n)                    : {n} students")
    print(f"  Math Mean ± SD                     : {math.mean():.2f} ± {math.std(ddof=1):.2f}")
    print(f"  Verbal Mean ± SD                   : {verbal.mean():.2f} ± {verbal.std(ddof=1):.2f}")
    print("-" * 68)
    print("  [CORRELATION METRICS]")
    print(f"  Pearson Correlation (r)            : {pearson_r:.4f} (R² = {r_squared:.4f})")
    print(f"  Spearman Rank Correlation (rho)    : {spearman_rho:.4f}")
    print("-" * 68)
    print("  [PAIRED DIFFERENCE METRICS (Math - Verbal)]")
    print(f"  Mean Difference ± 95% CI           : {mean_diff:+.2f} ± {ci_95:.2f}")
    print(f"  Std. Dev of Differences (s_d)      : {std_diff:.2f}")
    print(f"  Paired t-Statistic                 : t = {t_stat:.4f} (df = {n - 1})")
    print(f"  Effect Size (Cohen's d)            : d = {cohens_d:.4f}")
    print("-" * 68)
    print("  [STUDENT PERFORMANCE BREAKDOWN]")
    print(f"  Higher in Math                     : {math_higher} ({math_higher / n * 100:.1f}%)")
    print(f"  Higher in Verbal                   : {verbal_higher} ({verbal_higher / n * 100:.1f}%)")
    print(f"  Identical Scores                   : {tied} ({tied / n * 100:.1f}%)")
    print("=" * 68)


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    dataset_file = base_dir / 'dataset.txt'
    df_scores = load_dataset(dataset_file)
    analyze_paired_scores(df_scores)
