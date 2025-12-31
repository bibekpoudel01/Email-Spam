## 📧 Email Spam Detection Using Machine Learning
![Project Banner](Images/Front.jpg)

 Overview
 
Email spam is a persistent problem that affects productivity, security, and user experience. This project focuses on building a robust machine learning–based email spam classifier that can automatically distinguish between spam and legitimate (ham) emails. The solution applies classical NLP preprocessing techniques combined with multiple supervised learning algorithms and is deployed as an interactive web application using Streamlit Cloud.

The project emphasizes model comparison, performance evaluation, and real-world deployment, making it suitable for both academic learning and practical use cases.

# Problem Statement

Manual filtering of spam emails is inefficient and unreliable. Traditional rule-based filters often fail to adapt to evolving spam patterns. The objective of this project is to develop an automated, data-driven spam detection system that achieves high accuracy while maintaining strong recall for spam detection.

# Dataset Description

The dataset consists of labeled email messages categorized as:

0 – Ham (Not Spam)

1 – Spam

# Text Preprocessing & Feature Engineering

The raw email text was preprocessed using standard natural language processing techniques, including text cleaning, lowercasing, stopword removal, and tokenization. Visual insights were explored using word clouds to understand frequent terms in spam and ham emails. For numerical feature representation, TF-IDF vectorization was applied to capture the importance of words while reducing the impact of commonly occurring but less informative terms.

#  Machine Learning Models Used

Multiple machine learning algorithms were trained and evaluated to identify the most effective classifier:

1.Logistic Regression

2.Decision Tree Classifier

3.Random Forest Classifier

4.Gradient Boosting Classifier

5.AdaBoost Classifier

6.Naive Bayes (MultinomialNB)

7.XGBoost Classifier

After experimentation, Logistic Regression emerged as the best-performing model in terms of consistency, interpretability, and generalization.

# Model Evaluation

Model performance was evaluated using multiple metrics, including accuracy, precision, recall, F1-score, ROC-AUC score, and confusion matrix analysis. This multi-metric evaluation ensured that the model performed well not only in terms of overall accuracy but also in correctly identifying spam emails, which is critical for real-world applications.

# Hyperparameter Tuning

Hyperparameter tuning was performed to further optimize model performance and improve generalization on unseen data. Post-tuning analysis included ROC curve visualization and confusion matrix inspection, helping to validate the stability and robustness of the final selected model.

# Web Application & Deployment

An interactive web application was developed using Streamlit to allow users to input email text and get instant spam classification results. The app is deployed on Streamlit Cloud, making it accessible from anywhere without local setup.



![Deployment Demo](Images/Email%20Spam%20or%20Ham.png)






🔗 Try it live: https://email-spam-zm7nm2zwgmoxbnlw8sc5py.streamlit.app/


# Challenges Faced

During the project, several challenges were encountered, including handling class imbalance between spam and ham emails, preventing overfitting while maintaining high recall, and selecting an effective text feature representation. Additionally, deploying the machine learning model on Streamlit Cloud required resolving dependency and compatibility issues. These challenges were successfully addressed through careful experimentation, model tuning, and the application of best practices in NLP and deployment workflows.

#  Technologies Used

🐍 Python – core programming language used for data processing, modeling, and deployment

📊 Pandas, NumPy – data manipulation and numerical computations

🧠 Scikit-learn – machine learning models, TF-IDF vectorization, and evaluation metrics

📚 NLTK – text preprocessing and natural language processing tasks

🚀 XGBoost – advanced boosting algorithm for model comparison

📈 Matplotlib, Seaborn – data visualization, confusion matrix, and ROC curve plots

🌐 Streamlit – building the interactive web application

☁️ Streamlit Cloud – model deployment and public access

# Conclusion

This project demonstrates a complete end-to-end machine learning pipeline for email spam detection—from preprocessing and model training to deployment. Logistic Regression combined with TF-IDF proved to be a highly effective and reliable solution. The deployed application showcases how machine learning models can be translated into practical, user-facing tools.

