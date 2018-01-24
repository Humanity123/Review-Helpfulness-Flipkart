import numpy as np
import matplotlib.pyplot as plt
import sys
import os 

sys.path.append("../Parsers")
from rev_Parser import * 

def get_helpfulness_vs_deviation(product_reviews, absolute=True, fname="helpfulness_deviation_graph.png", fig_name = ""):
	''' function to get plot of review helpfulness vs the devation from average rating for a dictionary of producut reviews'''

	deviation_helpfulness_dic = {}
	for reviews in product_reviews.values():
		average_rating = round( np.mean([review['overall'] for review in reviews]) *2) / 2.0
		for review in reviews:
			deviation = review['overall'] - average_rating
			if absolute :
				deviation = abs(deviation)
			if deviation not in deviation_helpfulness_dic:
				deviation_helpfulness_dic[deviation] = [review['helpful']]
			else :
				deviation_helpfulness_dic[deviation].append(review['helpful'])

	x_values = deviation_helpfulness_dic.keys()
	x_values.sort()
	y_values = [deviation_helpfulness_dic[x_value] for x_value in x_values]
	
	fig, ax = plt.subplots()
	ax.set_title('Helpfulness vs Deviation from Average Star Rating: ' + fig_name)
	ax.boxplot(y_values, labels=x_values, whis = 0, showfliers=False)
	plt.savefig(fname, bbox_inches="tight")
	
	

def get_variance(reviews):
	''' returns the standard deviation of standard deviation of review's product rating rounded of to nearest 0.5 increment'''
	return round( (np.std([review['overall'] for review in reviews])**2) *2 ) / 2.0


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
	# reviews = get_review_data("/Users/yash/Documents/Acads/data/Flipkart/reviews_Electronics_5.json")
	reviews = get_review_data("/Users/yash/Documents/Acads/data/Flipkart/Sports_and_Outdoors_5.json")
	# reviews = get_review_data("/Users/yash/Documents/Acads/data/Flipkart/Cell_Phones_and_Accessories_5.json")	
	get_helpfulness_vs_deviation(reviews, True, "Absolute_Deviation_Graph_Sports"+".png")
	get_helpfulness_vs_deviation(reviews, False, "Signed_Deviation_Graph_Sports"+".png")
	variance_product_dic = get_variance_product_dic(reviews)
	for var in [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]:
		try:
			common_variance_products = variance_product_dic[var]
		except:
			continue
		target_product_review_dic = {}
		for product in variance_product_dic[var]:
			target_product_review_dic[product] = reviews[product]

		get_helpfulness_vs_deviation(target_product_review_dic, False, "Signed_Deviation_Graph_Sports"+str(var)+".png", str(var))

if __name__=='__main__':
	main()



