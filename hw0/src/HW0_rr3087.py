from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.metrics
from sklearn.metrics import f1_score
import sklearn.neighbors
import matplotlib.pyplot as plt
import numpy as np

print("Loading 20 newsgroups dataset for categories:")
data_train = fetch_20newsgroups(subset='train', shuffle=True, random_state=42)
data_test = fetch_20newsgroups(subset='test', shuffle=True, random_state=42)
print('data loaded')

'''Create tf-idf vectors for the input'''
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.9,
                                 stop_words='english')
X_train = vectorizer.fit_transform(data_train.data)
X_test = vectorizer.transform(data_test.data)
y_train = data_train.target
y_test = data_test.target

'''Train a K-Neighbors Classifier on the data'''
F1scores=[]
for i in range(2,51):
	n_neighbors = i
	weights = 'uniform'
	clf = sklearn.neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
	clf.fit(X_train, y_train)

	'''Make predictions on the test data using the trained classifier'''
	y_predicted = clf.predict(X_test)
	avg_f1 = f1_score(y_test, y_predicted, average='weighted')
	F1scores.append(avg_f1)

F1scores = np.array(F1scores)
NN = range(2,51)
plt.figure()
plt.xlabel('Num_Neighbours')
plt.xticks(np.arange(2,51))
plt.ylabel('F1 Score')
plt.plot(NN, F1scores)
plt.show()
# print ('Classification report:')
# print sklearn.metrics.classification_report(y_test, y_predicted,
                                            # target_names=data_test.target_names)
