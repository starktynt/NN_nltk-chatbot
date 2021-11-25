# -*- coding: utf-8 -*-


import nltk
import numpy as np
import random
import string
import warnings
warnings.filterwarnings("ignore")
import bs4 as bs
import urllib.request
import re
nltk.download('punkt')

#file1 = open('AI.txt', 'w')

raw_html = urllib.request.urlopen("https://en.wikipedia.org/wiki/Chatbot")


raw_html = raw_html.read()


article_html = bs.BeautifulSoup(raw_html, 'lxml')

article_paragraphs = article_html.find_all('p')

article_text = ''

for para in article_paragraphs:
    article_text += para.text


article_text = article_text.lower()


article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
type(article_paragraphs)


article_sentences = nltk.sent_tokenize(article_text)
article_words = nltk.word_tokenize(article_text)

print(article_text)





def app(arg):
  raw_html = urllib.request.urlopen(arg)


  raw_html = raw_html.read()


  article_html = bs.BeautifulSoup(raw_html, 'lxml')

  article_paragraphs = article_html.find_all('p')

  article_text = ''

  for para in article_paragraphs:
    article_text += para.text

  article_text = str(article_text)
  article_text = article_text.lower()


  article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
  article_text = re.sub(r'\s+', ' ', article_text)
  article_sentences = nltk.sent_tokenize(article_text)
  article_words = nltk.word_tokenize(article_text)
  #print(article_text)
  return (article_words)

def app_sentence(arg):
  raw_html = urllib.request.urlopen(arg)


  raw_html = raw_html.read()


  article_html = bs.BeautifulSoup(raw_html, 'lxml')

  article_paragraphs = article_html.find_all('p')

  article_text = ''

  for para in article_paragraphs:
    article_text += para.text

  article_text = str(article_text)
  article_text = article_text.lower()


  article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
  article_text = re.sub(r'\s+', ' ', article_text)
  article_sentences = nltk.sent_tokenize(article_text)
  article_words = nltk.word_tokenize(article_text)
  #print(article_text)
  return (article_sentences)


def app_textm(arg):
  raw_html = urllib.request.urlopen(arg)
  raw_html = raw_html.read()

  article_html = bs.BeautifulSoup(raw_html, 'lxml')
  article_paragraphs = article_html.find_all('p')
  article_text = ''

  for para in article_paragraphs:
    article_text += para.text
  
  article_text = str(article_text)
  article_text = article_text.lower()

  article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
  article_text = re.sub(r'\s+', ' ', article_text)
  article_sentences = nltk.sent_tokenize(article_text)
  article_words = nltk.word_tokenize(article_text)
  #print(article_text)
  return (article_text)



article_text   =  article_text + app_textm("https://en.wikipedia.org/wiki/United_States") + app_textm("https://en.wikipedia.org/wiki/Nature")

article_words = app("https://en.wikipedia.org/wiki/United_States") + app("https://en.wikipedia.org/wiki/Nature")

article_words = article_words + app("https://en.wikipedia.org/wiki/Human") +app("https://en.wikipedia.org/wiki/Earth")+app("https://en.wikipedia.org/wiki/Sun")

article_sentences = article_sentences + app_sentence("https://en.wikipedia.org/wiki/Human") +app_sentence("https://en.wikipedia.org/wiki/Earth")+app_sentence("https://en.wikipedia.org/wiki/Sun")

article_text = article_text + app_textm("https://en.wikipedia.org/wiki/Human") +app_textm("https://en.wikipedia.org/wiki/Earth")+ app_textm("https://en.wikipedia.org/wiki/Sun")

article_sentences = article_sentences + app_sentence("https://en.wikipedia.org/wiki/United_States") + app_sentence("https://en.wikipedia.org/wiki/Nature")

wnlemmatizer = nltk.stem.WordNetLemmatizer()

def perform_lemmatization(tokens):
    return [wnlemmatizer.lemmatize(token) for token in tokens]

punctuation_removal = dict((ord(punctuation), None) for punctuation in string.punctuation)

def get_processed_text(document):
    return perform_lemmatization(nltk.word_tokenize(document.lower().translate(punctuation_removal)))

greeting_inputs = ("hey", "HI", "good morning", "good evening", "morning", "evening", "hi", "whatsup","hello","howdy","you fine","what are you doing")
greeting_responses = ["Hey", "Hey Hows you?", "*Nods*", "Hello, How you doing", "Hello", "Welcome, I am good and you","Hello Ask me something ","Hey back bro"]

def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def generate_response(user_input):
    tennisrobo_response = ''
    article_sentences.append(user_input)

    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
    all_word_vectors = word_vectorizer.fit_transform(article_sentences)
    similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]

    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]

    if vector_matched == 0:
        tennisrobo_response = tennisrobo_response + "I am sorry ? Can you elborate please :p"
        return tennisrobo_response
    else:
        tennisrobo_response = tennisrobo_response + article_sentences[similar_sentence_number]
        return tennisrobo_response

nltk.download('wordnet')
word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
all_word_vectors = word_vectorizer.fit_transform(article_sentences)

similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)

similar_sentence_number = similar_vector_values.argsort()[0][-2]

continue_dialogue = True
print("Hello, I am your friend AI_BOT.You can ask me any question regarding a lot of things :")
while(continue_dialogue == True):
    human_text = input()
    human_text = human_text.lower()
    if human_text != 'bye':
        if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you bro':
            continue_dialogue = False
            print("AI_BOT: Most welcome")
        else:
            if generate_greeting_response(human_text) != None:
                print("AI_BOT: " + generate_greeting_response(human_text))
            else:
                print("AI_BOT: ", end="")
                print(generate_response(human_text))
                article_sentences.remove(human_text)
    else:
        continue_dialogue = False
        print("AI_BOT: Good bye and take care of yourself...")







