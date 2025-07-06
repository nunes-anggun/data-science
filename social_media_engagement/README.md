# Social Media Engagement Prediction

This project predicts whether a social media post will receive **high engagement** based on its metadata — including platform, post type, sentiment, day of week, and time category.

---

## Dataset

The dataset used in this project was sourced from [Kaggle](https://www.kaggle.com/)


## Goal

To classify posts as **high engagement** or **low engagement**, using only non-engagement features like platform, post type, sentiment, and posting time. The engagement score is based on the combined number of likes, comments, and shares.

---

## Machine Learning Models Used

We trained and compared multiple machine learning models:

- 🌳 Random Forest
- 📈 Logistic Regression
- ⚡ XGBoost
- 🔵 Support Vector Machine (SVM)
- 🟢 K-Nearest Neighbors (KNN)
- 🟠 Naive Bayes

Each model was evaluated using accuracy and confusion matrix.

---

## Results Summary

| Model                | Test Accuracy |
|----------------------|----------------|
| Random Forest         | 0.75 ✅          |
| Logistic Regression   | 0.75 ✅          |
| XGBoost               | 0.75 ✅          |
| Support Vector Machine| 0.75 ✅          |
| Naive Bayes           | 0.70 ⚠️          |
| K-Nearest Neighbors   | 0.40 ❌          |

✅ The best-performing models were **Random Forest**, **Logistic Regression**, and **XGBoost**.

---

## Insights

- Categorical features such as **platform**, **post type**, and **posting day** significantly influence engagement.
- Models trained with clean, engineered features achieved strong and consistent results.
- Simpler models like Naive Bayes and KNN struggled with this dataset.

---

## Model Export

Each model was saved using `joblib` for easy reuse. The best models can be loaded to make new predictions in future workflows.

---

## Next Steps

- Add more data to improve generalization
- Include time-based patterns (hour posted, recency)
- Possibly train on specific platforms separately

---

## Author

This project was completed as part of a machine learning portfolio to demonstrate classification, feature engineering, and model evaluation.

