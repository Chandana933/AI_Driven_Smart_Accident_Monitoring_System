import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_excel("../data/accident_dataset.xlsx")

X = df[['gasvalue','x_mems','y_mems']]
y = df['label_mems']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train,y_train)

joblib.dump(model,"../models/accident_model.pkl")

print("Model trained successfully")