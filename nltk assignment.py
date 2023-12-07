#texts 1,2,3

open("text_1.txt", "r")
open("text_2.txt", "r")
open("text_3.txt", "r")

#to determine 20 most common tokens from text
import nltk
a1 = nltk.most_common(text_1.txt)
a2 = nltk.most_common(text_2.txt)
a3 = nltk.most_common(text_3.txt)

#perform tokenization
from nltk import tokenize 
text1 = tokenize.word_tokenize(text_1.txt)
text2 = text1 = tokenize.word_tokenize(text_2.txt)
text3 = tokenize.word_tokenize(text_3.txt)

#perform stemming
from nltk.stem import porter
p = porter.PorterStemmer()
port_stem.stem(text_1.txt)
port_stem.stem(text_2.txt)
port_stem.stem(text_3.txt)

#perform lemmatization
from nltk.stem import wordnet
lemma = wordnet.WordNetLemmatizer()
wordnet_lemma.lemmatize(text_1.txt)
port_stem.stem(text_2.txt)
port_stem.stem(text_3.txt)

#determine the subject of the texts
#determine number of name entities in the text

from nltk import collections
n1 = collections.Counter(text_1.txt)
n2 = collections.Counter(text_2.txt)
n3 = collections.Counter(text_3.txt)

#determine the subject of the texts
x = nltk.pos_tag(ex_words, tagset = 'Universal')

#text 4

#perform n-gram analysis with n equal to 2 
x1 = nltk.ngrams(text_1.txt, 2)
x2 = nltk.ngrams(text_2.txt, 2)
x3 = nltk.ngrams(text_3.txt, 2)

