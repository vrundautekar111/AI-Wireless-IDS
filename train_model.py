import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

DATA_FILE = "wireless_intrusion_data.csv"

df = pd.read_csv(DATA_FILE)


print("=" * 60)
print("AI WIRELESS INTRUSION DETECTION SYSTEM")
print("=" * 60)

print("\nDataset loaded successfully.")

print("\nDataset shape:")
print(df.shape)

features = [

    "packet_rate",

    "deauth_rate",

    "failed_auth_attempts",

    "unique_source_count",

    "avg_signal_dbm",

    "connection_duration_sec",

    "retry_rate"

]


X = df[features]

y = df["label"]


X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)


print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


model = RandomForestClassifier(

    n_estimators=150,

    max_depth=12,

    random_state=42,

    class_weight="balanced"

)


print("\nTraining AI model...")

model.fit(
    X_train,
    y_train
)


print("Training completed.")


y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\n" + "=" * 60)

print(
    "MODEL ACCURACY:",
    round(accuracy * 100, 2),
    "%"
)


print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)


print("\nConfusion Matrix:")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)

MODEL_FILE = "wireless_ids_model.pkl"


joblib.dump(

    {
        "model": model,

        "features": features

    },

    MODEL_FILE

)


print("\nModel saved successfully.")

print(
    "File:",
    MODEL_FILE
)