import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("StudentsPerformance.csv")

df['Average score']= (df['math score'] +
                      df['reading score']+
                      df['writing score']) /3

df['Pass']= (df['Average score'] >= 60).astype(int)

encoder =LabelEncoder()

for col in df.select_dtypes(include="object").columns:
    df[col]= encoder.fit_transform(df[col])

X= df.drop("Pass", axis=1)
y= df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)

model.fit(X_train,y_train)

pickle.dump(model, open("model.pkl", "wb"))

print("Model Saved Successfully!")