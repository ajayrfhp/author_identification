from ingestor import *
import re
from feature_extractor import *
import numpy as np
import os
from sklearn.cross_validation import train_test_split

def prepare_X_y(data_path):
	'''
		READ RAW DATA, COMPUTE FEATURES AND SAVES X and y to numpy array locally
	'''
	data = ingest()
	list_features = compute_list_features(data)
	print len(list_features)
	X,y = convert_data_features(data,list_features)
	np.save(data_path + 'X.npy')
	np.save(data_path + 'y.npy')



cwd = os.getcwd()
data_path = cwd + '/author_identification/data/'
#prepare_X_y(data_path)

X = np.load(data_path + 'X.npy')
y = np.load(data_path + 'y.npy')

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_val, y_val, test_size=0.5, random_state=42)







