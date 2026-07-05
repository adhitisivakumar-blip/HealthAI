import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

# LOAD DATASET

df = pd.read_csv('datasets/Training.csv')

# REMOVE UNNECESSARY COLUMN

if 'Unnamed: 133' in df.columns:
    df = df.drop('Unnamed: 133', axis=1)

# FEATURES AND TARGET

X = df.drop('prognosis', axis=1)

y = df['prognosis']

# TRAIN TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)

# RANDOM FOREST MODEL

model = RandomForestClassifier()

model.fit(X_train, y_train)

# CREATE MODELS FOLDER IF NOT EXISTS

os.makedirs('models', exist_ok=True)

# SAVE MODEL

joblib.dump(model, 'models/disease_model.pkl')

print("Real AI Disease Prediction Model Trained Successfully")