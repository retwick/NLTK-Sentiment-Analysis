import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
stemmer_text  = "i missed you missing me colour coloured and colouring all the walls"


stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(EXAMPLE_TEXT)
ps = PorterStemmer()

#filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print("WORD TOKENS")
print(word_tokens)
print("FILTERED SENTENCE")
print(filtered_sentence)
for w in word_tokens:
	print(ps.stem(w))

#for x in filtered_sentence:
#	print(x) 

#print(sent_tokenize(EXAMPLE_TEXT))
