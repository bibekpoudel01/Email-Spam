## 📧 Email Spam Detection Using Machine Learning
 Overview
 
Email spam is a persistent problem that affects productivity, security, and user experience. This project focuses on building a robust machine learning–based email spam classifier that can automatically distinguish between spam and legitimate (ham) emails. The solution applies classical NLP preprocessing techniques combined with multiple supervised learning algorithms and is deployed as an interactive web application using Streamlit Cloud.

The project emphasizes model comparison, performance evaluation, and real-world deployment, making it suitable for both academic learning and practical use cases.

# Problem Statement

Manual filtering of spam emails is inefficient and unreliable. Traditional rule-based filters often fail to adapt to evolving spam patterns. The objective of this project is to develop an automated, data-driven spam detection system that achieves high accuracy while maintaining strong recall for spam detection.

# Dataset Description

The dataset consists of labeled email messages categorized as:

0 – Ham (Not Spam)

1 – Spam

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



# Web Application & Deployment

An interactive Streamlit web application was developed to allow users to input email text and instantly receive spam classification results.

The application is deployed on Streamlit Cloud, making it accessible from anywhere without local setup.

https://email-spam-zm7nm2zwgmoxbnlw8sc5py.streamlit.app/


# Challenges Faced

During the project, several challenges were encountered, including handling class imbalance between spam and ham emails, preventing overfitting while maintaining high recall, and selecting an effective text feature representation. Additionally, deploying the machine learning model on Streamlit Cloud required resolving dependency and compatibility issues. These challenges were successfully addressed through careful experimentation, model tuning, and the application of best practices in NLP and deployment workflows.

# Conclusion

This project demonstrates a complete end-to-end machine learning pipeline for email spam detection—from preprocessing and model training to deployment. Logistic Regression combined with TF-IDF proved to be a highly effective and reliable solution. The deployed application showcases how machine learning models can be translated into practical, user-facing tools.

https://email-spam-zm7nm2zwgmoxbnlw8sc5py.streamlit.app/
