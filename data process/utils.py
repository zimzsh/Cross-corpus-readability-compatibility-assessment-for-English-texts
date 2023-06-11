"""
utility functions for breaking down a given block of text
into it's component syntactic parts.
"""
import csv

import nltk
from nltk.tokenize import RegexpTokenizer
import syllables_en

TOKENIZER = RegexpTokenizer('(?u)\W+|\$[\d\.]+|\S+')
SPECIAL_CHARS = ['.', ',', '!', '?']

def readCorpus(path):
    corpus = []
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            corpus.append(row[0])
    return corpus

def get_char_count(words):
    characters = 0
    for word in words:
        characters += len(word.encode("utf-8").decode("utf-8"))
    return characters
    
def get_words(text=''):
    words = []
    words = TOKENIZER.tokenize(text)
    filtered_words = []
    for word in words:
        if word in SPECIAL_CHARS or word == " ":
            pass
        else:
            new_word = word.replace(",","").replace(".","")
            new_word = new_word.replace("!","").replace("?","")
            filtered_words.append(new_word)
    return filtered_words

def get_sentences(text=''):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(text)
    return sentences

def count_syllables(words):
    syllableCount = 0
    for word in words:
        syllableCount += syllables_en.count(word)
    return syllableCount

def count_complex_words(text=''):
    words = get_words(text)
    sentences = get_sentences(text)
    complex_words = 0
    found = False
    cur_word = []
    
    for word in words:          
        cur_word.append(word)
        if count_syllables(cur_word)>= 3:
            
            if not(word[0].isupper()):
                complex_words += 1
            else:
                for sentence in sentences:
                    if str(sentence).startswith(word):
                        found = True
                        break
                if found: 
                    complex_words += 1
                    found = False
                
        cur_word.remove(word)
    return complex_words

