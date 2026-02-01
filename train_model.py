
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_xgboost(df):
    X = df.drop('er_visit', axis=1)
    y = df['er_visit']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = xgb.XGBClassifier(eval_metric='logloss')
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"Model Accuracy: {acc}")
    return model
