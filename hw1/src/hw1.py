from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
import numpy as np
import scipy as sc  
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB, MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import re
from sklearn.externals import joblib
import sys
from analyze import analyze_model
from classify import classify_best_model


def read_dataset(filename): ## function to read the dataset in the correct format. 
	with open(filename) as f:
		dataset = f.read().splitlines()
	X = [i.split('\t')[0] for i in dataset]
	y = [i.split('\t')[1] for i in dataset]
	y = [0 if x=='democrat' else 1 for x in y]
	return X, y

Xtrain, ytrain = read_dataset('train_newline.txt')
Xtest, ytest = read_dataset('dev_newline.txt')

X = Xtrain + Xtest

stop_words_list = ENGLISH_STOP_WORDS.union([u'http', u'rt', u'amp', u'just', u'bit', u'ly', u'com', u'url', u'tinyurl', u'ow', u'twurl']) ## added these stop words
## after observing the top features in the different models 


### Uni-gram Model:
dic = CountVectorizer(input = X, ngram_range=(1,1), analyzer='word', stop_words=stop_words_list)

vecs = dic.fit_transform(X)

features = dic.fit(X).get_feature_names() ### getting the feature names of the different features to be used in the classifier.

trainvecs = vecs[0:40000,:]
testvecs = vecs[40000:,:]

clf = MultinomialNB() ## Using Multinomial Naive Bayes Classifier, which works well with text represented as word count vectors.

clf.fit(trainvecs, ytrain) 

sort_features = sorted(zip(clf.coef_[0], features), reverse=True) ### the coefficients have -ve values since log prob is calculated in multinomial NB

pred = clf.predict(testvecs)

print("UNIGRAM MODEL: \n")
print("Prediction Accuracy: ")
print(accuracy_score(ytest, pred))
print('\nThe Top-20 Features are: ')
for i in sort_features[0:20]:
	print(i) 
print('\nConfusion Matrix: ')
print(confusion_matrix(ytest, pred))


### Bi-gram Model:
dic = CountVectorizer(input = X, ngram_range=(2,2), analyzer='word', stop_words=stop_words_list)

vecs = dic.fit_transform(X)

features = dic.fit(X).get_feature_names() ### getting the feature names of the different features to be used in the classifier.

trainvecs = vecs[0:40000,:]
testvecs = vecs[40000:,:]

clf = MultinomialNB() ## Using Multinomial Naive Bayes Classifier, which works well with text represented as word count vectors.

clf.fit(trainvecs, ytrain) 

sort_features = sorted(zip(clf.coef_[0], features), reverse=True)

pred = clf.predict(testvecs)

print("\n\nBIGRAM MODEL: \n")
print("Prediction Accuracy: ")
print(accuracy_score(ytest, pred))
print('\nThe Top-20 Features are: ')
for i in sort_features[0:20]:
	print(i) 
print('\nConfusion Matrix: ')
print(confusion_matrix(ytest, pred))


### Tri-gram Model:
dic = CountVectorizer(input = X, ngram_range=(3,3), analyzer='word', stop_words=stop_words_list)

vecs = dic.fit_transform(X)

features = dic.fit(X).get_feature_names() ### getting the feature names of the different features to be used in the classifier.

trainvecs = vecs[0:40000,:]
testvecs = vecs[40000:,:]

clf = MultinomialNB() ## Using Multinomial Naive Bayes Classifier, which works well with text represented as word vector counts

clf.fit(trainvecs, ytrain) 

sort_features = sorted(zip(clf.coef_[0], features), reverse=True)

pred = clf.predict(testvecs)

print("\n\nTRIGRAM MODEL: \n")
print("Prediction Accuracy: ")
print(accuracy_score(ytest, pred))
print('\nThe Top-20 Features are: ')
for i in sort_features[0:20]:
	print(i) 
print('\nConfusion Matrix: ')
print(confusion_matrix(ytest, pred))

#### including the new added stop_words for the best model causes the accuracy to slightly reduce at alpha = 0.57

### Best Trained Model:
print("\n\nBEST TRAINED MODEL: \n")
classify_best_model('train_newline.txt', 'dev_newline.txt')
analyze_model('model.pkl', 'dev_newline.txt')
