import nltk
import random
import pickle
import sklearn
import time
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

start_time = time.time()

#get data
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
print("all words")
print(list(all_words.keys())[:10] )
#get top 3000 most common words using a freq distribution- 
word_features = list(all_words.keys())[:3000]

# get all words from doc. 
# set features as empty set
# loop through all word_features
# tell if features are present or not
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words) 

    return features

# featuresets contains Existence of a word(feature) and category( pos or neg) among all files in our dataset
featuresets = [(find_features(rev), category) for (rev, category) in documents]

# set that we'll train our classifier with
training_set = featuresets[:1900]

testing_set = featuresets[1900:]

##########################################################
###  CHOOSING A CLASSIFIER  ##############################
##########################################################

classifier = nltk.NaiveBayesClassifier.train(training_set)
#classifier.show_most_informative_features(30)
print('NB Classifier accuracy percent:',(nltk.classify.accuracy(classifier, testing_set)))


"""
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent:",nltk.classify.accuracy(MNB_classifier, testing_set))

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent:",nltk.classify.accuracy(BNB_classifier, testing_set))

print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set)))

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)))

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set)))

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set)))

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set)))



NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set)))
"""
print("Excecution time = %s" %(time.time() - start_time))

