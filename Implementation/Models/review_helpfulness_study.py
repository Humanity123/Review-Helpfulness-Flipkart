import numpy as np
import matplotlib.pyplot as plt
import sys
import os 

sys.path.append("../Parsers")
from rev_Parser import * 

def get_helpfulness_vs_deviation(reviews, absolute=True, fname="helpfulness_deviation_graph.png"):
	''' function to get plot of review helpfulness vs the devation from average rating'''

	average_rating = round( np.mean([review['overall'] for review in reviews]) *2) / 2.0
	deviation_helpfulness_dic = {}
	for review in reviews:
		deviation = review['overall'] - average_rating
		if absolute :
			deviation = abs(deviation)
		if deviation not in deviation_helpfulness_dic:
			deviation_helpfulness_dic[deviation] = [review['helpful']]
		else :
			deviation_helpfulness_dic[deviation].append(review['helpful'])

	x_values = deviation_helpfulness_dic.keys()
	y_values = [deviation_helpfulness_dic[x_value] for x_value in x_values]
	
	fig, ax = plt.subplots()
	ax.set_title('Helpfulness vs Deviation from Average Star Rating')
	ax.boxplot(y_values, labels=x_values, whis = 0, showfliers=False)
	plt.savefig(fname, bbox_inches="tight")
	
	

def get_variance(reviews):
	''' returns the standard deviation of standard deviation of review's product rating rounded of to nearest 0.5 increment'''
	return round( np.std([review['overall'] for review in reviews])*2 ) / 2.0


def get_variance_product_dic(product_review_dic):
	''' returns the dictionary with keys as variance and values as product ids'''
	variance_product_dic = {}
	for product, reviews in product_review_dic.iteritems():
		variance = get_variance(reviews)
		if variance not in variance_product_dic:
			variance_product_dic[variance] = [product]
		else:
			variance_product_dic[variance].append(product)

	return variance_product_dic


def main():
	reviews = get_review_data("")
	target_prod = ""
	for prod, rev_list in reviews.iteritems():
		if len(rev_list) > 100:
			target_prod = prod
			break
	get_helpfulness_vs_deviation(reviews[target_prod], True, "Absolute_Deviation_Graph.png")
if __name__=='__main__':
	main()




