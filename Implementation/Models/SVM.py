from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
import sys
sys.path.append("../Features")

import STR
import UGR
import GALC
import LIWC
import INQUIRER

STR_features_extractor = [get_STR_features]
UGR_features_extractor = [get_UGR_features]
GALC_features_extractor = [get_GALC_features]
LIWC_feature_extractor = [ get_LIWC_features]
INQUIRER_feature_extractor = [get_INQUIRER_features]
SEMANTIC_features_extractor = [get_GALC_features, get_LIWC_features, get_INQUIRER_features]
ALL_features_extractor = [get_STR_features, get_UGR_features, get_GALC_features, get_LIWC_features, get_INQUIRER_features]

def get_features(reviews, feature_extractors):
	''' function to get the feature vector of all the reviews
	according to the features given in the feature extractors, the features are concatenated to make
	a single feature vector for a review'''
	feature_vectors = None
	for feature_extractor in feature_extractors:
		if feature_vectors is None:
			feature_vectors = feature_extractor(reviews)
		else:
			feature_vectors = np.concatenate((feature_vectors, feature_extractor(reviews)), axis = 1)

	return feature_vectors


def get_labels(reviews):
	''' function to get the matrix of labels/values of the labelled reviews'''


def get_trained_SVR(reviews, labels, feature_extractors):
	''' function to get the trained SVR according to the given feature extractors'''
	X, Y = (get_features(reviews, feature_extractors), labels)
	svr  = SVR(kernel="rbf")
	svr.fit(X, Y)

	return svr

def test_SVR(reviews, labels, svr):
	''' function to test the trained SVR'''
	X, Y = (get_features(reviews, feature_extractors), labels)
	Y_pred = svr.predict(X)

	return mean_squared_error(Y, Y_pred)

def main():
	train_reviews, train_labels, test_reviews, test_labels = ()
	test_cases = [STR_features_extractor, UGR_features_extractor, GALC_features_extractor, LIWC_feature_extractor, INQUIRER_feature_extractor, SEMANTIC_features_extractor, ALL_features_extractor]
	test_case_results = []

	for test_case in test_cases:
		test_case_results.append(test_SVR(test_reviews, test_labels, get_trained_SVR(train_reviews, train_labels, test_case) ) )

	return test_case_results
	
if __name__ == "__main__"
	main()