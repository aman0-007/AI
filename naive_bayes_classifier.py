from sklearn.datasets import load_iris

iris = load_iris()
print(iris)

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4, random_state = 1)

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(x_train, y_train)

y_pred = gnb.predict(x_test)

from sklearn import metrics

print(f"GNB model accuracy(%): {metrics.accuracy_score(y_test, y_pred)*100}")