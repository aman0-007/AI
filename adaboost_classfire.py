import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['Invited', 'Mood', 'Weather', 'PartySize', 'Decision']
party_data = pd.read_csv("party_decision.csv", header = None, names = col_names)

feature_cols = ['Invited', 'Mood', 'Weather', 'PartySize']
X = party_data[feature_cols]
y = party_data.Decision

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

ada_party = AdaBoostClassifier(n_estimators = 6, learning_rate = 2)
ada_party = ada_party.fit(X_train, y_train)

y_pred = ada_party.predict(X_test)

print(f"y_test = {y_test}")
print(f"y_pred = {y_pred}")

print(f"Accuracy : {metrics.accuracy_score(y_test, y_pred)}")


new_data = [[
    int(input("Are you invited to the party? (1 = Yes, 2 = No): ")),
    int(input("Are you feeling happy or sad? (1 = Happy, 2 = Sad): ")),
    int(input("How's the weather? (1 = Nice, 2 = Bad): ")),
    int(input("What’s the size of the party? (1 = Small, 2 = Big): "))
]]
print(new_data)

y_new_pred = ada_party.predict(new_data)

print(f"y_new_pred = {y_new_pred}")