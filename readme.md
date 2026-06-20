# UPI Transaction Data Cleaner & Fraud Analyzer 🚀

An end-to-end data engineering and analytics pipeline built to process, clean, and analyze a simulated digital payments dataset containing **20,000 UPI transactions** representing over **₹1.75 Crore** in transaction volume.

This project demonstrates core competencies required for Technology Summer Analyst and Data Engineering roles, transitioning from exploratory Jupyter notebooks to production-ready automated Python scripts.

## 📊 Key Business Insights & Metrics Extracted
- **Rule-Based Risk Engine:** Engineered custom risk-scoring logic that successfully isolated **42 High-Risk transactions** (representing ₹80,409 in value) out of 20,000 total records, proving a highly tuned anomaly detection filter.
- **KYC Risk Vector:** Identified that non-verified users exhibited a fraud rate of **5.69%**, making them **1.6x more likely** to commit fraud compared to KYC-verified accounts (**3.52%**).
- **Temporal Vulnerabilities:** Discovered that 'Night' (**5.43%**) and 'Late Night' (**4.26%**) transactions carry nearly double the fraud risk of 'Morning' transactions (**2.87%**).
- **Platform Market Share vs. Risk:** Analyzed distribution across 6 payment apps. While GPay and PhonePe dominated volume (processing **12,302 combined transactions**), smaller platforms like WhatsApp Pay exhibited the highest proportional fraud rate (**4.35%**).

## 🛠️ Tech Stack & Engineering Practices
- **Languages & Libraries:** Python, Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn (Custom visual dashboards for Time, KYC, and App-based risk)
- **Engineering Principles:** Modular scripting (DRY), Data Pipeline Automation, Exploratory Data Analysis (EDA), Feature Engineering.

## 📁 Project Architecture
```text
upi-transaction-analyzer/
│
├── data/                   # Raw transaction datasets (Ignored in Git)
├── notebooks/              # Jupyter notebooks for EDA and feature engineering
│   └── analysis.ipynb
├── src/                    # Production-ready Python scripts
│   └── data_cleaning.py    # Automated cleaning pipeline
├── outputs/                # Cleaned CSVs and business summary reports
└── charts/                 # Matplotlib/Seaborn visual dashboards
```

## 🚀 How to Run the Data Pipeline

1. **Clone the repository:**

```bash
git clone https://github.com/Angadthakur/upi-transaction-analyzer.git
cd upi-transaction-analyzer
```

2. **Run the automated cleaning script:**

```bash
python src/data_cleaning.py
```
