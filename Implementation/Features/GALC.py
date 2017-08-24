from nltk import word_tokenize
import pandas as pd
import numpy as np

GALC_dic = {}
GALC_dimensions = 38 + 1

def get_GALC_dic(GALC_dic_loc):
	''' return the GALC dictionary using the saved GALC dictionary
	with key value same as the word roots and values as their index 
	in the feature vector'''
	df = pd.read_csv(GALC_dic_loc,dtype=str)
    for index, row in df.iterrows():
        for item in row[1:]:
            if not pd.isnull(item):
                if item.endswith('*'):
                    item = item[:-1]
                GALC_dic[item] = index
    
    return dic


def GALC(text):
	''' function to extract the GALC features of a review '''
	if not GALC_dic :
		raise ValueError("GALC dictionary is not loaded")
		
	features = [0]*GALC_dic
	words = word_tokenize(text)		
	for word in words:
		containsPrefix = False
		for prefix in GALC_dic.keys():
			if word.startswith(prefix):
				features[GALC_dic[prefix]] += 1
				containsPrefix = True
		
		if not containsPrefix:
			features[GALC_dimensions - 1] += 1

	return features


