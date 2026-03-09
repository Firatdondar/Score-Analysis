# 📊 Score Analysis

A Python script that reads student score data from a dataset and analyzes the relationship between Math and Turkish grades using correlation and average difference calculations.

---

## 📁 Project Structure

```
score-analysis/
├── analysis.py       # Main analysis script
├── dataset.txt       # Student scores dataset (100 students)
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## ✨ Features

- Loads real student data from a `.txt` dataset
- Calculates **Pearson correlation** between Math and Turkish scores
- Calculates the **average score difference** between the two subjects
- Clean and readable output

---

## 🚀 Installation & Usage

```bash
# 1. Clone the repository
git clone https://github.com/Firatdondar/score-analysis.git
cd score-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the analysis
python analysis.py
```

---

## 📤 Sample Output

```
Correlation between Math and Turkish scores: 0.3521...
Average difference between Math and Turkish: 4.0
```

---

## 🛠️ Requirements

- Python 3.8+
- numpy
- pandas
