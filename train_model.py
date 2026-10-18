import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

# Load dataset
df = pd.read_csv("eye_strain_dataset.csv")

# Encode target
y = df["strain_level"]
X = df.drop("strain_level", axis=1)

# Stratified split for balanced class performance
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# Pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(multi_class='ovr', class_weight='balanced', max_iter=300))
])

# Grid search to tune regularization strength
param_grid = {
    "clf__C": [0.1, 1, 5, 10]
}

grid = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

model = grid.best_estimator_
joblib.dump(model, "eye_strain_model.pkl")

# Predictions
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# Accuracy
print("Best Hyperparameters:", grid.best_params_)
print("Training Accuracy:", accuracy_score(y_train, train_pred))
print("Testing Accuracy:", accuracy_score(y_test, test_pred))

# Confusion matrix
cm = confusion_matrix(y_test, test_pred)
print("\nClassification Report:")
print(classification_report(y_test, test_pred))

sns.heatmap(cm, annot=True, cmap="Blues", fmt='d',
            xticklabels=["Low","Medium","High"],
            yticklabels=["Low","Medium","High"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()
