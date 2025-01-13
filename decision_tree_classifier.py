# for models 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# for tree
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

# col_names = ['Reservation', 'Raining', 'BadService', 'Saturday', 'Result']
# hoteldata = pd.read_csv("hotel for dtree.csv", header=None, names=col_names)
# feature_cols = ['Reservation', 'Raining', 'BadService', 'Saturday']
# X = hoteldata[feature_cols]
# y = hoteldata.Result

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

# clf = DecisionTreeClassifier(criterion = "entropy", max_depth = 5)
# clf = clf.fit(X_train, y_train)

# y_pred = clf.predict(X_test)

# print(f"ytest = {y_test}")
# print(f"y_pred = {y_pred}")

# print(f"Accuracy : {metrics.accuracy_score(y_test, y_pred)}")


col_names = ['Invited', 'Mood', 'Weather', 'PartySize', 'Decision']
partydata = pd.read_csv("party_decision.csv", header = None, names = col_names)
feature_cols = ['Invited', 'Mood', 'Weather', 'PartySize']

X = partydata[feature_cols]
y = partydata.Decision

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

ada_party = DecisionTreeClassifier(criterion = "entropy", max_depth = 5)
ada_party = ada_party.fit(X_train, y_train)

y_pred = ada_party.predict(X_test)

print(f"ytest = {y_test}")
print(f"y_pred = {y_pred}")

print(f"Accuracy : {metrics.accuracy_score(y_test, y_pred)}")

dot_data = StringIO()
export_graphviz(ada_party, out_file = dot_data, filled = True, rounded = True, feature_names= feature_cols, class_names = ['attending','not attending'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('party.png')

new_data = [[
    int(input("Are you invited to the party? (1 = Yes, 2 = No): ")),
    int(input("Are you feeling happy or sad? (1 = Happy, 2 = Sad): ")),
    int(input("How's the weather? (1 = Nice, 2 = Bad): ")),
    int(input("What’s the size of the party? (1 = Small, 2 = Big): "))
]]
print(new_data)

y_new_pred = ada_party.predict(new_data)

print(f"y_new_pred = {y_new_pred}")
