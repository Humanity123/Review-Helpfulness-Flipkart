from sklearn.svm import SVR
from sklearn import cross_validation
from sklearn.metrics import mean_squared_error
import os
from random import shuffle
import sys
sys.path.append("../Features")
sys.path.append("../Parsers")


from STR import *
from UGR import *
from GALC import *
from LIWC import *
from INQUIRER import *

from McParser import *

cmd_arg = sys.argv
data_dir = cmd_arg[1]

STR_features_extractor = [get_STR_features]
UGR_features_extractor = [get_UGR_features]
GALC_features_extractor = [get_GALC_features]
LIWC_feature_extractor = [ get_LIWC_features]
INQUIRER_feature_extractor = [get_INQUIRER_features]
SEMANTIC_features_extractor = [get_GALC_features, get_LIWC_features, get_INQUIRER_features]
ALL_features_extractor = [get_STR_features, get_UGR_features, get_GALC_features, get_LIWC_features, get_INQUIRER_features]

crt = os.path.join(os.getcwd(), "../../data/featureDictionaries/")

GALC_dic_loc = os.path.join(crt+"galc.csv")
INQUIRER_dic_loc = os.path.join(crt+"inquirerbasic.csv")
LIWC_dic_loc = os.path.join(crt+"LIWC2007.dic")
Start_Line = 66

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

def get_trained_SVR(reviews, labels, feature_extractors):
	''' function to get the trained SVR according to the given feature extractors'''
	X, Y = (get_features(reviews, feature_extractors), labels)
	svr  = SVR(kernel="rbf")
	svr.fit(X, Y)

	return svr

def test_SVR(reviews, labels, feature_extractors, svr):
	''' function to test the trained SVR'''
	X, Y = (get_features(reviews, feature_extractors), labels)
	Y_pred = svr.predict(X)

	return mean_squared_error(Y, Y_pred)


def main():
	direc_e = data_dir + "/electronics/"
	direc_b = data_dir + "/book/"
	direc_h = data_dir + "/home/"
	direc_o = data_dir + "/outdoor/"

	dir_list = [direc_b, direc_h, direc_o, direc_e]
	test_cases = [STR_features_extractor, UGR_features_extractor, GALC_features_extractor, LIWC_feature_extractor, INQUIRER_feature_extractor, SEMANTIC_features_extractor, ALL_features_extractor]

	get_GALC_dic(GALC_dic_loc)
	get_INQUIRER_dic(INQUIRER_dic_loc)
	get_LIWC_dic(LIWC_dic_loc, Start_Line)
	overall_result = []
	for c_dir in dir_list:
		rev_data = get_all_rev_data(c_dir)
		train_reviews, train_labels, test_reviews, test_labels = split_train_test_data(rev_data,1)
		test_case_results = []
		for test_case in test_cases:
			svr = SVR(kernel="rbf")
			test_case_results.append(cross_validation.cross_val_score(svr, get_features(train_reviews, test_case), train_labels, cv=10, scoring='mean_squared_error').mean())
		overall_result.append(test_case_results)
	overall_result = np.array(overall_result)
	print overall_result.mean(axis = 0)
	return overall_result
	
if __name__ == "__main__":
	main()