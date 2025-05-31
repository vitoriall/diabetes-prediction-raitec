from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def split_data(df):
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def get_model(name='decision_tree'):
    if name == 'random_forest':
        return RandomForestClassifier(n_estimators=100, random_state=42)
    elif name == 'logistic_regression':
        return LogisticRegression(max_iter=1000)
    else:
        return DecisionTreeClassifier(random_state=42)

def train_model(X_train, y_train, model_name='decision_tree'):
    model = get_model(model_name)
    model.fit(X_train, y_train)
    return model
