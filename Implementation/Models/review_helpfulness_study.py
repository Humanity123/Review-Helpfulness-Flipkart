import numpy as np
import matplotlib.pyplot as plt

def get_helpfulness_vs_deviation(reviews, absolute=True):
	''' function to get plot of review helpfulness vs the devation from average rating'''

	average_rating = np.mean([reviews.overall for review in reviews])
	deviation_helpfulness_dic = {}
	for review in reviews:
		deviation = review.overall - average_rating
		if absolute :
			devation = abs(deviation)
		if devation not in deviation_helpfulness_dic:
			deviation_helpfulness_dic[deviation] = [review.helpfulness]
		else :
			deviation_helpfulness_dic[deviation].append(review.helpfulness)

	x_values = deviation_helpfulness_dic.keys()
	y_values = [np.mean(deviation_helpfulness_dic[x_value]) for x_value in x_values]
	y_lower  = [y_values[index] - np.min(deviation_helpfulness_dic[x_value]) for index, x_value in enumerate(x_values)] 
	y_upper  = [np.max(deviation_helpfulness_dic[x_value]) - y_values[index] for index, x_value in enumerate(x_values)] 
	helpfulness_vs_deviation_plot = plt.errorbar(x_values, y_values, yerr=[y_lower, y_upper])
	return helpfulness_vs_deviation_plot

def get_variance(reviews):
	''' returns the standard deviation of standard deviation of review's product rating rounded of to nearest 0.5 increment'''
	return round( np.std([review.overall for review in reviews])*2 ) / 2.0





