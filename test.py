import csv
import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize

ifile = open('small_data.csv', "rb")
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

    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#Read the tweets one by one and process it


"""
input_data = raw_input("give me some text.\n")
print("Processed data:")
print(processTweet(input_data))
"""







PosWordFileVar = open("pos.txt",'w')
NegWordFileVar = open("neg.txt", 'w')

data = [] 
rownum = 0
for row in reader:
# Save header row.
	if rownum == 0:
		header = row
	else:
		#print '%s: %s' % (header[colnum], row[3])
		data.append([row[3], row[1]])
 		print("Processed tweet")
        print ( processTweet(row[3]))
        #print("Word tokenize")

        for x in sent_tokenize(processTweet(row[3])):
            x += "\n"
            if row[1] == '1':
                PosWordFileVar.write(x)
            else:
                NegWordFileVar.write(x)

	rownum += 1

PosWordFileVar.close()
NegWordFileVar.close()


PosWordFileVar = open("pos.txt", 'r')
NegWordFileVar = open("neg.txt", 'r')

#print("\nDATA \n")
#print(data)

"""
PUT THIS BAAAAAAAAAACK

all_words_var = []
for x in AllWordFile_Var:
    all_words_var.append(x)
"""

#fdist = nltk.FreqDist(all_words_var)
# write all words to AllWordFile






#freq_words = nltk.FreqDist(data)[:5]
#get top 3000 most common words using a freq distribution- 
#word_features = list(freq_words.keys())[:3000]

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
 
ifile.close()
