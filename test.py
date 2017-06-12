import csv
import nltk
import re
import sklearn
import re
from collections import Counter
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from autocorrect import spell



NO_OF_FEATURES = 5000
DATA_SPLIT = 0.80


ifile = open('Sentiment Analysis Dataset.csv', "rb")
reader = csv.reader(ifile)

#start process_tweet
def processTweet(tweet):
    # process the tweets

    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #remove numbers
    tweet = re.sub('[0-9]', ' ',tweet)
    #remove common symbols
    tweet = re.sub('[!-&;=-]', ' ',tweet)
    #remove multiple dots
    tweet = re.sub('\.\.+', '',tweet)
    #remove crappy symbols
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    tweet = pattern.sub(r"\1\1", tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

AllWordFileVar = open("allwords.txt",'w')
print("writing to all files")

data = [] 

rownum = 0
for row in reader:   # Save header row.
	if rownum == 0:
		header = row
	else:
		row[3] = unicode(row[3], errors='ignore')
		row[3] = processTweet(row[3])
		dummy_var = ''
        	for x in word_tokenize(row[3]):
            		dummy_var += spell(x) + " "
        	data.append([dummy_var,row[1]])
        	AllWordFileVar.write(dummy_var + "\n")

	rownum += 1


AllWordFileVar.close()

print("finished writing to pos and neg files")
print("reading from files")

AllWordFileVar = open("allwords.txt", 'rb')
StopWordsFileVar = open("stop_words.txt",'rb')

AllWordsVar = nltk.word_tokenize(AllWordFileVar.read())

    
# Remove single-character tokens (mostly punzctuation)
AllWordsVar = [word for word in AllWordsVar if (len(word) > 1 ) ]

stop_words_var = word_tokenize(StopWordsFileVar.read())
AllWordsVar = [x for x in AllWordsVar if not x in stop_words_var]

fdist = nltk.FreqDist(AllWordsVar)
features = []

########################################################################################################
#        set number of features to NO_OF_FEATURES
########################################################################################################
for word,frequency in fdist.most_common(NO_OF_FEATURES):
    features.append(word)
    #print(u'{} - {}'.format(word, frequency))

# tell if features are present or not
def find_features(content):
    words = word_tokenize(content)
    #print("\nwords")
    #print(words)
    check_features = {}
    for w in features:
        check_features[w] = (w in words) 

    return check_features


#get top 3000 most common words using a freq distribution- 
all_data = []
for (x,y) in data:
    all_data.append((find_features(x) , y))

#print (all_data)
DATA_LEN =  len(data)
training_data = all_data[:DATA_SPLIT*DATA_LEN]
testing_data = all_data[DATA_SPLIT*DATA_LEN:]

classifier = NaiveBayesClassifier.train(training_data)
accuracy = nltk.classify.util.accuracy(classifier, testing_data)
print("Finally your programme compiled and got an accuracy of: ")
print(accuracy)


manual_test = find_features("i am happy")
print("The classifier says its:")
print(classifier.classify(manual_test))



AllWordFileVar.close()
StopWordsFileVar.close() 
ifile.close()