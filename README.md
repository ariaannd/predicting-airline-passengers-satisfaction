# Airline Passenger Satisfaction Prediction

Created by Aria Ananda

## Project Overview
This project aims to build a machine learning model to predict airline passenger satisfaction for Japan Airlines. We'll evaluate several classification models to identify the best approach for accurate and reliable predictions. Database from this project used from kaggle.com

### Models Explored:
1. **K-Nearest Neighbor (KNN)**
2. **Support Vector Machine (SVM)**
3. **Decision Tree**
4. **Random Forest**
5. **XGBoost (XGBClassifier)**

Each model will be evaluated using cross-validation and performance metrics like the **F1 score**. After identifying the best base model, we'll fine-tune its hyperparameters for enhanced performance.

## Workflow
1. **Data Preprocessing**: Handle missing values, feature encoding, and normalization.
2. **Model Evaluation**:
   - Train the models using cross-validation.
   - Evaluate with performance metrics (F1 score, accuracy, precision, recall).
3. **Model Tuning**: Fine-tune hyperparameters of the best base model using grid search or random search.
4. **Comparison**: Compare the tuned model against the base model to select the most accurate and reliable model.

## Results
Final model performance will be measured based on:
- **F1 Score**
- **Accuracy**
- **Precision**
- **Recall**

## Conclusion
The best-performing model after tuning will be selected for final deployment, providing a robust solution for predicting airline passenger satisfaction.