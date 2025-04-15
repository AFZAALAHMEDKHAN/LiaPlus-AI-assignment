from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data and train model
X, y = load_iris(return_X_y=True)
clf = RandomForestClassifier()
clf.fit(X, y)

# Save the trained model
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)
