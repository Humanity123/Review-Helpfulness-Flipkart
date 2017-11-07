import json
from collections import defaultdict

def get_review_data(file_path):
	reviews = []
	for line in open(file_path, 'r'):
		reviews.append(json.loads(line))
	answer = defaultdict(lambda: list())
	count = 0
	for review in reviews:
		votes = review['helpful']
		# if votes[1]==0:
		# 	continue
		if votes[1] < 10:
			continue		
		count += 1
		review['helpful'] = votes[0]*1.0/votes[1]
		answer[review['asin']].append({'helpful':review['helpful'], 'overall':review['overall']})
	print count
	return answer

def main():
	get_review_data("/Users/yash/Documents/Acads/data/Cell_Phones_and_Accessories_5.json")

if __name__=='__main__':
	main()
