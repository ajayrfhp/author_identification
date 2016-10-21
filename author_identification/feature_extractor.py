import re
from collections import Counter
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

def compute_list_features(data):
	'''
		IDENTIFIES WORDS WITH FREQUENCY >=5 ACROSS DOCUMENTS AND RETURNS THE WORDS
	'''
	word_str = ''
	targets = data.keys()
	for target in targets:
		word_str = word_str + ' '.join(data[target])
	
	word_str = re.sub(r'[^\w\s]','',word_str)	
	word_list = word_str.split(' ')
	
	all_features = Counter(word_list)
	filtered_features = dict(filter(lambda x:x[1]>=10, all_features.items())).keys()
	print filtered_features
	return filtered_features

def convert_data_features(data,list_features):
	'''
		GIVEN DATA DICTIONARY AND LIST OF FEATURES, COMPUTE FEATURE VECTOR FOR EACH ROW IN DATA 
	'''
	X = []
	y = []
	enc = LabelEncoder()
	print data.keys()
	enc.fit(data.keys())
	for target in data.keys():
		print target
		for sentence in data[target]:
			
			vec = np.zeros((1,len(list_features)))	
			for i in range(len(list_features)):
				vec[0,i] = sentence.count(list_features[i])
			X.append(vec)
			y.append(enc.transform([target]))
	X = np.array(X)
	X = X.reshape((X.shape[0],X.shape[2]))
	y = np.array(y)
	y = y + 1		
	return X, y
	

	
