import numpy as np
from nltk import word_tokenize

LIWC_dic = {}
LIWC_prefixes = []
LIWC_dim = 0

def create_LIWC_dim_maps(path, dim_map):
	global LIWC_dim
	dim_idx = 0
	with open(path) as f:
		for i, l in enumerate(f):
			if i == 0:
				continue
			l = l.strip()
			if l == '%':
				break
			given_dim = l.split('\t')[0]
			dim_map[given_dim] = dim_idx
			dim_idx += 1
		LIWC_dim = dim_idx

def compute_prefixes(path, start_line):
	global LIWC_prefixes
	with open(path) as f:
		for i, l in enumerate(f):
			if i < start_line:
				continue
			target = l.strip().split('\t')[0]
			if target.endswith('*'):
				LIWC_prefixes.append(target[:-1])

def create_dictionary(path, start_line, dim_map):
	global LIWC_dic
	with open(path) as f:
		for i, l in enumerate(f):
			if i < start_line:
				continue
			l = l.strip().split('\t')
			word, dim = l[0], l[1:]

			if word.endswith('*'):
				word = word[:-1]

			actual_dims = np.zeros(LIWC_dim)
			for d in dim:
				actual_dims[dim_map[d]]=1
			LIWC_dic[word] = actual_dims

def get_LIWC_dic(LIWC_dic_loc, start_line):
	dim_map = {}
	create_LIWC_dim_maps(LIWC_dic_loc, dim_map)
	compute_prefixes(LIWC_dic_loc, start_line)
	create_dictionary(LIWC_dic_loc, start_line, dim_map)

def LIWC(text):
	global LIWC_dim, LIWC_dic, LIWC_prefixes
	if not LIWC_dic :
		raise ValueError("LIWC dictionary is not loaded!!")

	features = np.zeros(LIWC_dim)
	words = word_tokenize(text)		
	for word in words:
		word_small = word.lower()
		if word_small in LIWC_dic:
			features += LIWC_dic[word_small]
		else:
			for prefix in LIWC_prefixes:
				if word.startswith(prefix):
					features += LIWC_dic[prefix]
					break
	return features