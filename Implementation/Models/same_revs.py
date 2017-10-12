#!/usr/bin/python
import gensim
import sys
import heapq
from nltk.tokenize import word_tokenize
sys.path.append("../Parsers")

from rev_Parser import * 

cmd_arg = sys.argv
data_dir = cmd_arg[1]

def get_features(raw_documents):
	gen_docs = [[w.lower() for w in word_tokenize(text)] for text in raw_documents]
	dictionary = gensim.corpora.Dictionary(gen_docs)
	corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
	tf_idf = gensim.models.TfidfModel(corpus)
	sims = gensim.similarities.Similarity('/home/kushagra/Documents/BTP/my_work/Review-Study-Amazon/Analysis/', tf_idf[corpus], num_features=len(dictionary))
	return sims

def get_ids_reviews():
	raw_documents = []
	ids = []

	reviews = get_review_data(data_dir)

	for review in reviews:
		ids.append(review['reviewerID'])
		raw_documents.append(review['reviewText'])

	return ids, raw_documents

def get_index_similarity_matrix(sims, ids):
	top_sim = []
	for crt, sim in enumerate(sims):
		L = [(i[0],i[1]) for i in sorted(enumerate(sim), key=lambda x:x[1], reverse=True) if ids[crt]!=ids[i[0]]]
		top_sim.append([entry for entry in L if entry[0]!=entry[1]][:500])
		# top_sim.append(L[:500])
	return top_sim


def main():
	ids, raw_documents = get_ids_reviews()
	ids = ids[:1000]
	raw_documents = raw_documents[:1000]
	print("Number of documents:",len(raw_documents))
	print "Getting Bag of Words -> tf-idf"
	sims = get_features(raw_documents)
	print "Tf-Idf Retrieved..."
	print "Getting similarities matrix...	"
	ans = get_index_similarity_matrix(sims,ids)
	print "Got Similarity Matrix"
	print "Getting top matches..."
	matches_f = [ (ids[crt],ids[elem[0][0]], elem[0][1])  for crt, elem in enumerate(ans)]
	matches_sorted = sorted(matches_f, key=lambda x:x[2], reverse=True) 
	print matches_sorted[:20]
	print "======================="
	print matches_sorted[200:220]
	print "===============0========"
	print matches_sorted[400:420]
	print "======================="
	print matches_sorted[600:620]
	print "======================="
	print matches_sorted[800:820]
	print len(matches_sorted)

if __name__ == '__main__':
	main()