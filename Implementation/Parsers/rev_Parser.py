import json
from collections import defaultdict

def get_review_data(file):
	reviews = []
	for line in open("/home/kushagra/Documents/BTP/my_work/crawled_data/Cell_Phones_and_Accessories_5.json", 'r'):
		reviews.append(json.loads(line))
	answer = defaultdict(lambda: list())
	for review in reviews:
		votes = review['helpful']
		if votes[1]==0:
			continue
		review['helpful'] = votes[0]*1.0/votes[1]
		answer[review['asin']].append(review)
	return answer

def main():
	get_review_data("/home/kushagra/Documents/BTP/my_work/crawled_data/Cell_Phones_and_Accessories_5.json")

if __name__=='__main__':
	main()