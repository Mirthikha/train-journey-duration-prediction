# Train Journey Duration Prediction 🚆

## 📌 Project Overview
This project focuses on predicting train journey duration using machine learning techniques.  
The goal is to analyze how the number of input features affects model performance by comparing models trained with **one feature** and **two features**.

A user-friendly **Streamlit web interface** is also developed to allow users to input values and view predictions interactively.

---

## 🎯 Objective
- To build a regression model for predicting train journey duration
- To compare model performance using:
  - Single feature
  - Two features
- To visualize results and predictions using an interactive UI

---

## 📂 Dataset
- Dataset contains information related to train journeys
- Features used:
  - Feature 1: Distance (example)
  - Feature 2: Average Speed (example)
- Target variable:
  - Journey Duration

*(Note: Feature names may vary based on dataset)*

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Loaded the dataset
- Handled missing values
- Selected relevant features

### 2. Feature Selection
- Model 1: Trained using **one feature**
- Model 2: Trained using **two features**

### 3. Model Training
- Used **Linear Regression**
- Split data into training and testing sets

### 4. Model Evaluation
Models were evaluated using:
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### 5. User Interface
- Built an interactive interface using Streamlit
- Users can input feature values
- The app displays predicted journey duration

---

## 📊 Model Comparison
| Model Type | Features Used | Performance |
|-----------|--------------|-------------|
| Model 1 | Single Feature | Lower accuracy |
| Model 2 | Two Features | Improved accuracy |

**Observation:**  
The model trained with two features performed better, as it captures more information affecting journey duration.

---

## 📈 Results
- Two-feature model showed:
  - Lower error values
  - Higher R² score
- This confirms that adding relevant features improves prediction performance

---

## 🖥️ User Interface (Streamlit App)
The Streamlit interface allows:
- Easy input of journey details
- Real-time prediction results
- Clear comparison between model outputs

This makes the project more user-friendly and practical.

---

## 🚀 How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/Mirthikha/train-journey-duration-prediction.git
