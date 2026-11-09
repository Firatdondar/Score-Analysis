# 📈 Paired Score Correlation & Difference Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?logo=numpy&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A statistical evaluation tool in Python (**Pandas** & **NumPy**) that performs bivariate correlation analysis (**Pearson $r$** and **Spearman $\rho$**), paired score difference testing (**Paired $t$-statistic**), and standardized effect size estimation (**Cohen's $d$**) across student exam results.

---

## ✨ Key Features

- **Parametric & Non-Parametric Correlation:** Computes both **Pearson's linear correlation ($r$)** with coefficient of determination ($R^2$) and **Spearman's rank correlation ($\rho$)**.
- **Paired Difference Hypothesis Testing:** Evaluates within-student performance differentials ($\Delta = \text{Math} - \text{Verbal}$), standard error of the mean difference ($\text{SE}_{\bar{d}}$), 95% confidence intervals, and the paired $t$-statistic.
- **Effect Size Quantification:** Calculates **Cohen's $d$** to measure the practical magnitude of inter-subject score differences.
- **Dominance Breakdown:** Categorizes students by subject dominance (Higher in Math vs. Higher in Verbal vs. Tied).

---

## 🗂️ Project Structure

```text
Score-Analysis/
├── analysis.py              # Paired statistical analysis & reporting script
├── dataset.txt              # Tab-separated student exam dataset (n = 100)
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/Firatdondar/Score-Analysis.git
cd Score-Analysis
pip install -r requirements.txt
python analysis.py
```

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.
