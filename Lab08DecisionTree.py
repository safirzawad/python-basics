# author 15301093 Safir Zawad

import pandas as pd

csv_input = pd.read_csv('data.csv')

csv_input['Taste'] = csv_input['Color']
csv_input['Taste'] = csv_input['Taste'].replace('Red', 'Sweet')
csv_input['Taste'] = csv_input['Taste'].replace('Blue', 'Bitter')

csv_input.to_csv('newdata.csv', index=False)

data = read_csv("newdata.csv")

data['Color'] = data['Color'].map({'Red': 0, 'Blue': 1})
data['Brand'] = data['Brand'].map({'Snickers': 0, 'Kit Kat': 1})
data['Taste'] = data['Taste'].map({'Bitter': 0, 'Sweet': 1})

predictors = ['Color', 'Brand', 'Taste']

X = data[predictors]
Y = data.Class

decisionTreeClassifier = tree.DecisionTreeClassifier(criterion="entropy")
dTree = decisionTreeClassifier.fit(X, Y)

dotData = tree.export_graphviz(dTree, out_file=None)
print(dotData)

print(dTree.predict([[1, 1, 0]]))
(print(dTree.predict([[0, 0, 1]])))
