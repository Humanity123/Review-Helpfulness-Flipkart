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