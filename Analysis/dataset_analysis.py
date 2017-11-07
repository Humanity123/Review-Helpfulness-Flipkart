import numpy as np
import json

def average_reviews(product_reviews):
	''' returns the avg reviews per product '''
	return np.mean([len(reviews) for reviews in product_reviews])

def star_rating_distribution(product_reviews):
	'''returns the star_rating distribution information for product and product reviews'''
	review_star_rating_dict ={1.0:0, 2.0:0, 3.0:0, 4.0:0, 5.0:0}
	product_star_rating_dict={1.0:0, 2.0:0, 3.0:0, 4.0:0, 5.0:0}
	product_ratings         = []

	for reviews in product_reviews:
		product_ratings.append(np.mean([review['star_rating'] for review in reviews]))
		product_star_rating_dict[round(product_ratings[-1])] += 1

		for review in reviews:
			review_star_rating_dict[review['star_rating']] += 1

	review_star_rating_dict['mean'] = np.sum([key*value for key,value in review_star_rating_dict.items()]) / np.sum(review_star_rating_dict.values())
	product_star_rating_dict['mean'] = np.mean(product_ratings)

	return (review_star_rating_dict, product_star_rating_dict)

def main():
	with open("/Users/yash/Documents/Acads/BTP/data/reviews/camera_data/uk/camera_uk_dict.txt", "r") as review_file:
		review_list = json.load(review_file)
	product_reviews = []
	reviews = []
	for index, review in enumerate(review_list):
		if index == 0:
			reviews = [review]
			continue
		elif review_list[index]['product_id'] == review_list[index-1]['product_id']:
			reviews.append(review)
		else:
			product_reviews.append(reviews)
			reviews = [review]
	product_reviews.append(reviews)

	star_ratings_analysis = star_rating_distribution(product_reviews)
	dataset_analysis = {
		'average_reviews': average_reviews(product_reviews),
		'review_star_rating_dict': star_ratings_analysis[0],
		'product_star_rating_dict': star_ratings_analysis[1]
	} 
	return dataset_analysis

if __name__ == "__main__":
	main()

	

	
