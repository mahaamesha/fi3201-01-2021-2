from sklearn import svm

# features
x = [
  [1, 1],
  [1, 2],
  [1, 3],
  [2, 1],
  [2, 2],
  [2, 3],
  [3, 1],
  [3, 2],
  [3, 3],
]

# labels
y = [0, 0, 0, 0, 1, 1, 1, 1, 1]

# fil
clf = svm.SVC(kernel='linear').fit(x, y)

# predict
p = clf.predict([[4, 4]])
print(p)

p = clf.predict([[0, 0]])
print(p)

p = clf.predict([[0, 4]])
print("Prediction result:", p)