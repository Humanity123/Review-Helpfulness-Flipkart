from random import shuffle
import os
import numpy as np

def get_rev_data(file):
	''' returns pair of review and real valued score in the given file'''
	score = 0
	text = ""
	with open(file, "r") as fobj:
		line = fobj.readline()
		val = line.split(" ")[1].rstrip().split("/")
		score = float(val[0])/float(val[1])
		fobj.readline()
		fobj.readline()
		for line in fobj:
			text = text + line.rstrip()
		text = " ".join(text.split()[1:])
	return score, text

def get_all_rev_data(dir):
	''' returns list of pair of all review data in the directory '''
	reviews_data = []
	for dirname, dirs, files in os.walk(dir):
		for filename in files:
			if filename.endswith("review"):
				reviews_data.append(get_rev_data(dir+filename))
	return reviews_data

def split_train_test_data(reviews_data, split_factor):
	''' review data is a list of pair of review and its score '''
	''' Splits the the data into train and test data randomly as per split ratio'''
	shuffle(reviews_data)
	scores_reviews = zip(*reviews_data)
	scores = np.array(scores_reviews[0])
	reviews = np.array(scores_reviews[1])
	return reviews[:int(len(reviews)*split_factor)], scores[:int(len(scores)*split_factor)], reviews[int(len(reviews)*split_factor):], scores[int(len(scores)*split_factor):]