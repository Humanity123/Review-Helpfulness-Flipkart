import os
from random import shuffle

def get_rev_data(file):
	''' returns pair of review and real valued score in the given file'''
	score = 0
	text = ""
	with open(file, "r") as fobj:
		line = fobj.readline()
		val = line.split(" ")[1].rstrip().split("/")
		score = float(val[0])/float(val[1])
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
	scores = scores_reviews[0]
	reviews = scores_reviews[1]
	return reviews[0:int(len(reviews)*split_factor)], scores[0:int(len(scores)*split_factor)], reviews[int(len(reviews)*split_factor)+1:int(len(reviews))-1], scores[int(len(scores)*split_factor)+1:int(len(scores))-1]