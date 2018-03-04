from sklearn.feature_extraction.text import CountVectorizer
import numpy as np 
import scipy as sc  
from sklearn import svm
from sklearn.naive_bayes import BernoulliNB, MultinomialNB, GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import re
from sklearn.externals import joblib
import sys


def get_non_ascii_count(dataset): ### Function for counting the number of non-ascii characters
	c = [len(re.findall("[^\x00-\x7F]", i, flags=re.UNICODE)) for i in dataset]
	return np.array(c).reshape(len(c),1)

def get_emoji_count(dataset): ### Funtion for counting a collection (not all) of emojis.
	c = [len(re.findall(": \)|: \(|: D|: p", i, flags=re.UNICODE)) for i in dataset]
	return np.array(c).reshape(len(c),1)

def get_happy_face_count(dataset): ### Function for counting a happy face emoji :)
	c = [len(re.findall(": \)", i, flags=re.UNICODE)) for i in dataset]
	return np.array(c).reshape(len(c),1)

def get_sad_face_count(dataset): ### Function for counting a sad face emoji :(
	c = [len(re.findall(": \(", i, flags=re.UNICODE)) for i in dataset]
	return np.array(c).reshape(len(c),1)

def get_D_face_count(dataset): ### Function for counting :D emoji
	c = [len(re.findall(": D", i, flags=re.UNICODE)) for i in dataset]
	return np.array(c).reshape(len(c),1)

def get_p_face_count(dataset): ### Function for counting :p emoji
	c = [len(re.findall(": p", i, flags=re.UNICODE)) for i in dataset]
	return np.array(c).reshape(len(c),1)	

def get_excl_count(dataset): ### Function for counting ! marks
	c = [len(re.findall("!", i, flags=re.UNICODE)) for i in dataset]
	return np.array(c).reshape(len(c),1)

def get_2ndhappy_face_count(dataset): ### Function for counting ;) emoji
	c = [len(re.findall("; \)", i, flags=re.UNICODE)) for i in dataset]
	return np.array(c).reshape(len(c),1)
 
def read_dataset(filename): ## function to read the dataset in the correct format. 
	with open(filename) as f:
		dataset = f.read().splitlines()
	X = [i.split('\t')[0] for i in dataset]
	y = [i.split('\t')[1] for i in dataset]
	y = [0 if x=='democrat' else 1 for x in y]
	return X, y

def analyze_model(model, testset):
	Xtrain, ytrain = read_dataset('train_newline.txt')
	Xtest, ytest = read_dataset(testset)

	X = Xtrain + Xtest

	dic = CountVectorizer(input = X, ngram_range=(1,3), analyzer='word', stop_words='english', lowercase='False') ### Not converting all text to lowercase, helps to count the Capital words as well.

	vecs = dic.fit_transform(X)

	features = dic.fit(X).get_feature_names() ### getting the feature names of the different features to be used in the classifier.

	trainvecs = vecs[0:40000,:]
	testvecs = vecs[40000:,:]

	### Creating feature vectors for new features from the Train set
	c1train = get_emoji_count(Xtrain)
	c2train = get_non_ascii_count(Xtrain)
	c3train = get_happy_face_count(Xtrain)
	c4train = get_sad_face_count(Xtrain)
	c5train = get_D_face_count(Xtrain)
	c6train = get_p_face_count(Xtrain)
	c7train = get_excl_count(Xtrain)
	c8train = get_2ndhappy_face_count(Xtrain)

	### Creating feature vectors for new features from the Test set
	c1test = get_emoji_count(Xtest)
	c2test = get_non_ascii_count(Xtest)
	c3test = get_happy_face_count(Xtest)
	c4test = get_sad_face_count(Xtest)
	c5test = get_D_face_count(Xtest)
	c6test = get_p_face_count(Xtest)
	c7test = get_excl_count(Xtest)
	c8test = get_2ndhappy_face_count(Xtest)

	trainvecs = sc.sparse.hstack((trainvecs, c2train, c3train, c4train, c7train, c8train)) ### Adding new features to the whole sparse feature matrix

	testvecs = sc.sparse.hstack((testvecs, c2test, c3test, c4test, c7test, c8test))

	features.extend(('Non_Ascii_Characters', 'Happy_Face_Emojis', 'Sad_Face_Emojis', 'Exclamation_!', '2nd_Happy_Face_;)')) ### updating the features names

	clf = joblib.load(model)  ### loading the saved pickle model

	sort_features = sorted(zip(clf.coef_[0], features), reverse=True)

	pred = clf.predict(testvecs)

	print("\nPrediction Accuracy: ")
	print(accuracy_score(ytest, pred))
	print('\nThe Top-20 Features are: ')
	for i in sort_features[0:20]:
		print(i) 
	print('\nConfusion Matrix: ')
	print(confusion_matrix(ytest, pred))
	print('\n')


if __name__ == '__main__':
	analyze_model(str(sys.argv[1]), str(sys.argv[2]))
