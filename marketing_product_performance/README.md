# Revenue Prediction with Feature Engineering and Random Forest

## Overview

This project explores the challenge of predicting `Revenue_Generated` using marketing and campaign features such as budget, units sold, and clicks. The dataset initially showed weak predictive signals (R² ≈ -0.03), but through **log-transformation** and **feature engineering**, the model achieved a **cross-validated R² of 0.9975**, indicating strong generalization.

This is a **Data Science project**, highlighting the power of modeling, feature engineering, and validation in understanding business performance.

---

## Objectives

- Predict revenue with regression models.
- Handle poor feature correlation and skewed target.
- Engineer meaningful features for better model performance.
- Validate model robustness with cross-validation.

---

## Dataset

> *Kaggle* marketing dataset

Features include:
- `Budget`
- `Clicks`
- `Units_Sold`
- `Subscription_Tier`
- `Discount_Level`
- `Revenue_Generated` *(target)*

---

## Feature Engineering

Created new features:
- `Revenue_per_Unit`
- `Revenue_per_Budget`
- `Revenue_per_Click`
- `Discount_Percent`
- `Log_Revenue` *(log-transformed target)*

---

## Model

- Model: `RandomForestRegressor`
- Preprocessing: One-hot encoding + log transformation
- Validation: 5-fold cross-validation

### Results

| Metric          | Value       |
|-----------------|-------------|
| R² (Train/Test) | 0.9969      |
| CV R² (5-fold)  | 0.9975      |

 No signs of overfitting. Performance is consistent across folds.

---

##  Top Features

- `Revenue_per_Unit`
- `Revenue_per_Budget`
- `Revenue_per_Click`
- `Units_Sold`
- `Budget`
- `Clicks`

These features show that **efficiency** matters more than raw values.

---

## Visuals

- Feature importance plot
- Log revenue distribution
- Scatterplots (optional)

---

## Conclusion

This project shows that even when the original data quality is poor, thoughtful **feature engineering** and **target transformation** can dramatically improve model performance.

It reflects real-world data science thinking — not just chasing metrics, but reshaping the problem to make it solvable.

---

## Tools Used

- Python (Pandas, NumPy, Scikit-learn, Matplotlib)
- Jupyter Notebook
- Anaconda

---

## Future Improvements

- Add time-based features (e.g. seasonality)
- Collect better data on product category or customer segmentation
- Try interpretable models like SHAP

---

## License

MIT License

