from ingestor import *
import re
from feature_extractor import *
import numpy as np
import os
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


def prepare_X_y(data_path):
	'''
		READ RAW DATA, COMPUTE FEATURES AND SAVES X and y to numpy array locally
	'''
	data = ingest()
	list_features = compute_list_features(data)
	print len(list_features)
	X,y = convert_data_features(data,list_features)
	np.save(data_path + 'X.npy',X)
	np.save(data_path + 'y.npy',y)



cwd = os.getcwd()
data_path = cwd + '/author_identification/data/'
prepare_X_y(data_path)

X = np.load(data_path + 'X.npy')
y = np.load(data_path + 'y.npy')
X = preprocessing.scale(X)

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_val, y_val, test_size=0.5, random_state=42)



####### BUILD MODELS


clf = svm.SVC()
clf.fit(X_train,y_train)

predictions = clf.predict(X_train)

training_error = accuracy_score(predictions,y_train)
print 'TRAINING ERRORS'
print confusion_matrix(predictions,y_train)
print training_error
print clf.score(X_train, y_train)
val_predictions = clf.predict(X_val)

print 'VALIDATION ERRORS'
validation_error = accuracy_score(val_predictions,y_val)
print confusion_matrix(val_predictions,y_val)
print validation_error
print clf.score(X_val,y_val)




