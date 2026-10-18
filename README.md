# VisionGuard: Eye Strain Risk Prediction

### Machine Learning-Based Digital Eye Strain Risk Prediction Using Logistic Regression

VisionGuard is a machine learning mini-project that predicts the risk of digital eye strain based on users' daily screen usage habits. It uses Logistic Regression to classify eye-strain risk into **Low, Medium, and High** categories and provides personalized suggestions to encourage healthier screen habits.

## 📌 Project Overview

Prolonged screen exposure, high brightness, insufficient breaks, and small font sizes may contribute to digital eye strain. VisionGuard provides an interactive web application where users enter their screen usage habits and receive a predicted risk level along with preventive recommendations.

## ✨ Features

- **Eye Strain Risk Prediction:** Classifies risk into Low, Medium, or High.
- **Interactive User Interface:** Uses Streamlit sliders and dropdowns.
- **Multiple Input Parameters:** Evaluates screen time, brightness, breaks per hour, font size, and blue-light filter usage.
- **Personalized Recommendations:** Provides suggestions based on the predicted risk.
- **Machine Learning Model:** Uses Logistic Regression for classification.
- **Model Optimization:** Uses feature scaling, class balancing, and GridSearchCV.
- **Performance Evaluation:** Supports accuracy, classification reports, and confusion matrix analysis.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and preprocessing |
| Streamlit | Interactive web interface |
| Joblib | Saving and loading the trained model |
| Matplotlib | Visualization |
| Seaborn | Confusion matrix visualization |

## 📂 Project Structure

```text
VisionGuard-Eye-Strain-Prediction/
│
├── app.py                  # Streamlit web application
├── train_model.py          # Model training and evaluation
├── eye_strain_dataset.csv  # Eye-strain dataset
├── eye_strain_model.pkl    # Saved machine learning model
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── SCRIPT_CODE.pdf         # Project code documentation
```

## ⚙️ Input Features

| Feature | Description |
|---|---|
| Screen Time | Daily screen usage in hours |
| Brightness | Screen brightness percentage |
| Breaks per Hour | Number of breaks taken per hour |
| Font Size | Display font size in pixels |
| Blue-Light Filter | Whether the blue-light filter is enabled |

## 🔄 Working Methodology

1. Collect screen usage inputs from the user.
2. Process the input features for the machine learning model.
3. Apply the trained Logistic Regression model.
4. Predict the eye-strain risk category.
5. Display the result and preventive recommendations.

**Workflow:**

User Input → Feature Processing → Logistic Regression Model → Risk Prediction → Recommendations

## 🚀 Installation and Setup

### Prerequisites

- Python 3.9 or later
- pip package manager
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/indiraparadkar675/VisionGuard-Eye-Strain-Prediction.git
```

### Step 2: Navigate to the Project Folder

```bash
cd VisionGuard-Eye-Strain-Prediction
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## 🧠 Train the Model Again

To retrain the model using the available dataset, run:

```bash
python train_model.py
```

The trained model will be saved as `eye_strain_model.pkl`.

**Note:** The saved model file must be present in the project directory before running `app.py`.

## 📊 Model Evaluation

The project report records a test accuracy of **96%** for the Logistic Regression model. Performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

Actual performance may vary depending on the dataset, data quality, and evaluation procedure.

## 🎯 Project Objectives

- Predict eye-strain risk using machine learning.
- Understand the relationship between screen usage habits and predicted risk.
- Provide accessible preventive recommendations.
- Develop a lightweight application using Python and Streamlit.

## 🔮 Future Enhancements

- Collect and evaluate more real-world user data.
- Include ambient lighting, viewing distance, and blink-rate features.
- Add historical predictions and habit-tracking graphs.
- Develop a mobile application or browser extension.
- Validate the model with appropriate real-world studies.


---

⭐ If you find this project interesting, consider giving the repository a star!
