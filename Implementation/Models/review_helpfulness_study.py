import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("../Parsers")
from rev_Parser import * 

def get_helpfulness_vs_deviation(reviews, absolute=True):
	''' function to get plot of review helpfulness vs the devation from average rating'''

	average_rating = np.mean([review['overall'] for review in reviews])
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
	y_values = [np.mean(deviation_helpfulness_dic[x_value]) for x_value in x_values]
	y_lower  = [y_values[index] - np.min(deviation_helpfulness_dic[x_value]) for index, x_value in enumerate(x_values)] 
	y_upper  = [np.max(deviation_helpfulness_dic[x_value]) - y_values[index] for index, x_value in enumerate(x_values)] 
	helpfulness_vs_deviation_plot = plt.errorbar(x_values, y_values, yerr=[y_lower, y_upper])
	print x_values
	print y_values
	plt.show()
	return helpfulness_vs_deviation_plot

def get_variance(reviews):
	''' returns the standard deviation of standard deviation of review's product rating rounded of to nearest 0.5 increment'''
	return round( np.std([review['overall'] for review in reviews])*2 ) / 2.0

def main():
	reviews = get_review_data("/home/kushagra/Documents/BTP/my_work/crawled_data/Cell_Phones_and_Accessories_5.json")
	target_prod = ""
	for prod, rev_list in reviews.iteritems():
		if len(rev_list) > 100:
			target_prod = prod
			break
	get_helpfulness_vs_deviation(reviews[target_prod], True)
if __name__=='__main__':
	main()




