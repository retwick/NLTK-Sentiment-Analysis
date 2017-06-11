import nltk
import random
import pickle
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

#get top 3000 most common words using a freq distribution- 
word_features = list(all_words.keys())[:5]
print(word_features)
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
#featuresets = [(find_features(rev), category) for (rev, category) in documents]

# set that we'll test against.
testing_set = featuresets[1200:]

#load previously saved classifier
#classifier_file = open("NB.pickle", "rb")
#classifier = pickle.load(classifier_file)

#print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

classifier_file.close()


# random shuffle is done twice, which has increased the accuracy by testing some training data



