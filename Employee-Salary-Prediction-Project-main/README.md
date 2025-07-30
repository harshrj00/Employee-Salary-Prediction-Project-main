<p align="center">
  <img src="https://github.com/user-attachments/assets/432f4916-f707-4ccc-9b5e-0770abf9362b" alt="Edunet Foundation" height="45" style="margin-right: 15px;">
  <img src="https://github.com/user-attachments/assets/65734ff1-9bed-49fd-b433-cd5a624e1707" alt="Shell Logo" height="45">
</p>


# Employee Salary Prediction App

A Streamlit-powered web app that predicts whether an individual's annual salary is likely to exceed ₹50,000 based on demographic and financial attributes. Built during internship at Edunet Foundation under IBM SkillBuild mentorship.

---
## Project Preview:
**View-1**
<img width="1909" height="985" alt="image" src="https://github.com/user-attachments/assets/435433d9-ec65-4b9b-84ba-2e0005165d13" />
**View-2**
<img width="1916" height="983" alt="image" src="https://github.com/user-attachments/assets/55f1e493-0718-4b66-b800-f6f1fd140fbe" />

https://github.com/user-attachments/assets/32e03397-a262-4ed8-ae3b-63c27d14f6cd

https://github.com/user-attachments/assets/eb37dd0b-7194-4025-9a8e-ef9696a808fb

Try it now:-https://employee-salary-prediction-project.onrender.com/

-----------------------------
## Features
- Clean and branded UI with Edunet & IBM logos
- Animated result feedback (balloons , snow )
- Human-readable dropdowns for categorical features
- Full input summary with prediction result
- Integrated ML model trained on the Adult dataset
- Deployable via platforms like Render

---
## Dataset Overview
The model was trained using the Adult Income dataset, sourced from the UCI Machine Learning Repository. It contains over 32,000 records with 15 features including:
- Age, workclass, education level, marital status
- Occupation, relationship, race, gender
- Capital gain/loss, hours worked per week, country
- Income class (≤₹50,000 or >₹50,000)
> All categorical data was encoded using LabelEncoder for compatibility with scikit-learn models.

---
##  Data Preprocessing
- Removed rows with missing values (? symbols) across workclass, occupation, and native country
- Encoded categorical variables using LabelEncoder for compatibility with scikit-learn
- Scaled numerical features for balanced model convergence
- Splitting the dataset into training (80%) and testing (20%) to ensure reliable evaluation
-----------
## Model Comparison & Selection
Before finalizing the Gradient Boosting model, several algorithms were evaluated for accuracy, precision, and reliability. Here's a summary:
| Model                    | Accuracy | Notes                                    |
|--------------------------|----------|------------------------------------------|
| Logistic Regression      | ~79%     | Fast and interpretable, but underfit     |
| Decision Tree            | ~82%     | Good baseline, prone to overfitting      |
| Random Forest            | ~84%     | Stable performance, slower than GBM      |
| Gradient Boosting (final)| ~85%     | Best trade-off between accuracy & speed  |
- Gradient Boosting Classifier was selected for its superior performance on both training and validation sets.
- All models were trained and tested on the preprocessed Adult dataset using an 80/20 split.
- Accuracy and other metrics were computed using classification_report and cross-validation.
> This comparison demonstrates thoughtful experimentation before deployment — aligning with best practices in machine learning workflow.
------------
## Model Building — Gradient Boosting Classifier
| Parameter       | Value    |
|----------------|----------|
| Model           | GradientBoostingClassifier |
| `n_estimators`  | 100      |
| `learning_rate` | 0.1      |
| `max_depth`     | 3        |
| `random_state`  | 42       |
| Encoding        | LabelEncoder on categorical features |
| Deployment      | Pickle model (`best_model.pkl`) loaded into `app.py` |

- Gradient Boosting was chosen for its robust performance and ability to reduce bias & variance
- Trained using the cleaned and encoded dataset on all features
- Final model serialized with pickle as best_model.pkl
------------------
## Feature Importance
Top contributing features identified by the model:
1. Age  
2. Education Level  
3. Hours per Week  
4. Capital Gain  
5. Occupation  
> These attributes most significantly influence income prediction
----------------
## Evaluation Summar
| Metric     | Value  |
|------------|--------|
| Accuracy   | ~85%   |
| Precision  | 0.86   |
| Recall     | 0.83   |
| F1-Score   | 0.84   |
## Why Gradient Boosting?
- Combines multiple weak learners into a strong predictive model
- Handles categorical and numeric features efficiently
- Performs better than simple decision trees in generalization and precision
> The final model was exported using pickle and loaded in the deployed app through app.py.

--------
##  Project Structure
```
Employee-Salary-Prediction-Project/
├── app.py          # Main Streamlit app 
├── employee salary prediction.ipynb  # Model training notebook 
├── best_model.pkl               # Serialized trained ML model 
├── adult.csv                    # Cleaned dataset 
├── requirements.txt             # All dependencies 
├── README.md                    # This file
```
----------------
##  Sample Input vs Predicted Output
| Feature             | Sample Value        |
|---------------------|---------------------|
| Age                 | 35                  |
| Workclass           | Private             |
| Education Level     | Bachelors           |
| Marital Status      | Married             |
| Occupation          | Exec-managerial     |
| Relationship        | Husband             |
| Race                | White               |
| Gender              | Male                |
| Capital Gain        | 5000                |
| Capital Loss        | 0                   |
| Hours Per Week      | 45                  |
| Native Country      | India               |

### Predicted Output
>  **Predicted Salary:** More than ₹50,000/year  
>  *Congratulations! You're projected to earn above the threshold!*

---

##  Installation & Run Guide
### Setup Instructions

1. **Clone the repository**
```
   git clone https://github.com/Siteshgupta123/Employee-Salary-Prediction-Project.git
   cd Employee-Salary-Prediction-Project
```
2. **Create a virtual environment (optional but recommended)**
```
python -m venv venv
venv\Scripts\activate   # On Windows
```
3. **Install dependencies**
```
pip install -r requirements.txt
```
4.**Run the app**
```
streamlit run app.py
```
-------------------
## Acknowledgment:
Special thanks to **[Channabasava Yadav Sir](https://www.linkedin.com/in/channabasava-yadav-2b1a06b0/)** , **[Dr.Nanthini Mohan Ma’am](https://www.linkedin.com/in/dr-nanthini-mohan-9a727a105/)** for their continued mentorship throughout the internship. This project gave me real-world experience in sustainable analytics and AI/ML pipeline development.

-----------------
## Deployment
You can deploy this project on **Render**, **Streamlit Community Cloud**, or any hosting platform that supports Python + Streamlit.

-----------
## Thank You! 

Thanks for checking out my project! If you found it useful, please consider:  
[![GitHub stars](https://github.com/Siteshgupta123)] 
- **Starring** the repo  
-  **Reporting** issues  
-  **Contributing** improvements  

Coded by **Sitesh Gupta**  
🔗 www.linkedin.com/in/guptasitesh |  Email-guptasitesh05@email.com

-------------------------------------------
