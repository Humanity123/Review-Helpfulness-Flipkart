from nltk import word_tokenize
import pandas as pd
import numpy as np

INQUIRER_dic = {}
INQUIRER_drop_columns = ['Source', 'Othtags', 'Defined']
INQUIRER_dim = 182

def get_INQUIRER_dic(INQUIRER_dic_loc):
	''' return the INQUIRER dictionary using the saved INQUIRER dictionary
	with key value same as the word roots and values as their feature vector'''
	df = pd.read_csv(INQUIRER_dic_loc,dtype=str)
	df = df.drop(INQUIRER_drop_columns, axis = 1)
	
	if len(df.columns[1:]) is not INQUIRER_dim :
		raise ValueError("INQUIRER dictionary contains different number of features as assumed")

	for index, row in df.iterrows():
		INQUIRER_dic[row[0]] = np.array(~ pd.isnull(row[1:]), dtype=float)


def INQUIRER(text):
	''' function to extract the INQUIRER features of a review 
	currently the word or word+#1 is looked in the INQUIRER dictionary
	for features
	might explore better ways to idetify which form of word to use such as WORD#2 etc'''
	if not INQUIRER_dic :
		raise ValueError("INQUIRER dictionary is not loaded")

	features = np.zeros(INQUIRER_dim)
	words = word_tokenize(text)		
	for word in words:
		word_caps = word.upper()
		if word_caps in INQUIRER_dic:
			features += INQUIRER_dic[word_caps]
		elif (word_caps+"#1") in INQUIRER_dic:
			features += INQUIRER_dic[word_caps+"#1"]

	return features


def get_INQUIRER_features(reviews, INQUIRER_dic_loc=None):
	''' function to get the matrix of features of all reviews '''
	if INQUIRER_dic_loc is None:
		get_INQUIRER_dic(INQUIRER_dic_loc)
	features_vectors = []

	for review in reviews:
		features_vectors.append(INQUIRER(review))

	return np.array(features_vectors, dtype=float)