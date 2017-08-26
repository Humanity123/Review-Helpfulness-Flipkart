from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

from collections import defaultdict

def tf_idf_matrix(reviews):

	# split all reviews into lists
	texts = [[word for word in document.lower().split()] for document in reviews]

	#calculating total word frequency over all documents
	d=defaultdict(int)
	for lister in texts:
	    for item in lister:
	        d[item]+=1

	# remove words that appear only once
	tokens=[key for key,value in d.items() if value>2]
	
	filter_reviews = [" ".join([word for word in document if word in tokens]) for document in texts]
	# texts = [[word for word in document if word in tokens] 

	vectorizer = TfidfVectorizer(ngram_range=(1,1), stop_words=stopwords.words('english'))
	return vectorizer.fit_transform(filter_reviews)

#for testing
def main():
	documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]
	ok = tf_idf_matrix(documents)
	# print "hello"
	print(ok)

if __name__ == '__main__':
	main()