import csv
import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

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
    tweet = re.sub('[0-9]', '',tweet)
    #remove common symbols
    tweet = re.sub('(!)|(-)', '',tweet)
    #remove multiple dots
    tweet = re.sub('\.\.+', '',tweet)
    #remove crappy symbols

    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end




PosWordFileVar = open("pos.txt",'w')
NegWordFileVar = open("neg.txt", 'w')

print("writing to pos and neg files")

data = [] 
rownum = 0
for row in reader:
# Save header row.
	if rownum == 0:
		header = row
	else:
		data.append([row[3], row[1]])
 		#print("Processed tweet")
        #print ( processTweet(row[3]))
        #print("Word tokenize")
        row[3] = unicode(row[3], errors='ignore')

        for x in sent_tokenize(processTweet(row[3])):
            x += "\n"
            if row[1] == '1':
                PosWordFileVar.write(x)
            else:
                NegWordFileVar.write(x)

	rownum += 1

PosWordFileVar.close()
NegWordFileVar.close()

print("finished writing to pos and neg files")
print("reading from files")

PosWordFileVar = open("pos.txt", 'r')
NegWordFileVar = open("neg.txt", 'r')
StopWordsFileVar = open("stop_words.txt",'r')

AllWordsVar = nltk.word_tokenize(PosWordFileVar.read())
AllWordsVar += nltk.word_tokenize(NegWordFileVar.read())
    
# Remove single-character tokens (mostly punctuation)
AllWordsVar = [word for word in AllWordsVar if (len(word) > 1 ) ]

stop_words_var = word_tokenize(StopWordsFileVar.read())
AllWordsVar = [x for x in AllWordsVar if not x in stop_words_var]

#print(features)

fdist = nltk.FreqDist(AllWordsVar)
features = []



########################################################################################################
#        set number of features to 10
########################################################################################################
for word,frequency in fdist.most_common(15):
    features.append(word)
    #print(u'{} - {}'.format(word, frequency))

#print(features)





#get top 3000 most common words using a freq distribution- 


# get all words from doc. 
# set features as empty set
# loop through all word_features
# tell if features are present or not

def find_features(content):
    words = word_tokenize(content)
    print("\nwords")
    print(words)
    check_features = {}
    for w in features:
        check_features[w] = (w in words) 

    return check_features

print(find_features("oh my good this is good i have a feeling of love"))


PosWordFileVar = close()
NegWordFileVar = close()
StopWordsFileVar = close() 


ifile.close()
