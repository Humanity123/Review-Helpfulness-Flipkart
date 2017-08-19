from nltk import sent_tokenize, word_tokenize

def STR(text):
	''' function to extract structural features from a review as per 
	Kim et al., 2006; Xiong and Litman, 2011 '''
	sentences = sent_tokenize(text)
	words, question_sentences, exclam_sentences = (0.0, 0.0, 0.0)

	for sentence in sentences:
		tokens = word_tokenize(sentence)
		words += len(tokens)
		if tokens[-1] == "?":
			question_sentences += 1
		if tokens[-1] == "!":
			exclam_sentences   += 1

	average_sentence_len = words/len(sentences)
	return (words, len(sentences), average_sentence_len, question_sentences, exclam_sentences)

