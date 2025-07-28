import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
import os
import json

records = [json.loads(line) for line in open("data/labeled_features.jsonl", encoding="utf-8")]
df = pd.DataFrame(records)


X = df[["size","gap","width","text_len","is_bold","ends_with_colon","has_digits","is_title_case"]]
y = df["label"]


X_train,X_val,y_train,y_val = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

model = LGBMClassifier(n_estimators=100, num_leaves=16, learning_rate=0.1, class_weight="balanced"
)
model.fit(X_train, y_train)

from sklearn.metrics import classification_report
print(classification_report(y_val, model.predict(X_val)))

os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/gbt_model.pkl","wb"))
print("✅ Model saved to model/gbt_model.pkl")