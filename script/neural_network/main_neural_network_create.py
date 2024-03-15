import pandas as pd
import numpy as np
import pymorphy3
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from collections import Counter
import pickle


nltk.download('punkt')
nltk.download('stopwords')


max_words = 10000
random_state = 42


classes = open('classes.txt', 'r', encoding='utf-8').readlines()
train = pd.read_csv('train.csv', usecols=[0,2])
test = pd.read_csv('test.csv', usecols=[0,2])


def preprocess(text, stop_words, punctuation_marks, morph):
    tokens = word_tokenize(text.lower())
    preprocessed_text = []
    for token in tokens:
        if token not in punctuation_marks:
            lemma = morph.parse(token)[0].normal_form
            if lemma not in stop_words:
                preprocessed_text.append(lemma)
    return preprocessed_text


punctuation_marks = ['!', ',', '(', ')', ':', '-', '?', '.', '..', '...', '«', '»', ';', '–', '--']
stop_words = stopwords.words("russian")
morph = pymorphy3.MorphAnalyzer()


punctuation_marks = ['!', ',', '(', ')', ':', '-', '?', '.', '..', '...', '«', '»', ';', '–', '--']
stop_words = stopwords.words("russian")
morph = pymorphy3.MorphAnalyzer()


test['Preprocessed_texts'] = test.apply(lambda row: preprocess(row['text'], punctuation_marks, stop_words, morph), axis=1)
train['Preprocessed_texts'] = train.apply(lambda row: preprocess(row['text'], punctuation_marks, stop_words, morph), axis=1)


for txt in test['Preprocessed_texts']:
    words.update(txt)
for txt in train['Preprocessed_texts']:
    words.update(txt)
word_to_index = dict()
index_to_word = dict()


for i, word in enumerate(words.most_common(max_words - 2)):
    word_to_index[word[0]] = i + 2
    index_to_word[i + 2] = word[0]


def text_to_sequence(txt, word_to_index):
    seq = []
    for word in txt:
        index = word_to_index.get(word, 1) # 1 означает неизвестное слово
        # Неизвестные слова не добавляем в выходную последовательность
        if index != 1:
            seq.append(index)
    return seq


test['Sequences'] = test.apply(lambda row: text_to_sequence(row['Preprocessed_texts'], word_to_index), axis=1)
train['Sequences'] = train.apply(lambda row: text_to_sequence(row['Preprocessed_texts'], word_to_index), axis=1)


mapping = {'World': 1, 'Sports': 2, 'Business': 3, 'Sci/Tech': 4}


x_train_seq = train['Sequences']
y_train = train['score']


x_test_seq = test['Sequences']
y_test = test['score']


def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        for index in sequence:
            results[i, index] += 1.
    return results


x_train = vectorize_sequences(x_train_seq, max_words)


x_test = vectorize_sequences(x_test_seq, max_words)


lr = LogisticRegression(random_state=random_state, max_iter=200)
lr.fit(x_train, y_train)


pkl_model = 'pickle_model.h5'
with open(pkl_model, 'wb') as file:
  pickle.dump(lr, file)



topic = open('C:/Users/Владимир/Desktop/projectMain_S/script/data/new_vk_messages.txt', 'r', encoding='utf-8').read()


preprocessed_text = preprocess(testStr, stop_words, punctuation_marks, morph)
seq = text_to_sequence(preprocessed_text, word_to_index)
bow = vectorize_sequences([seq], max_words)


print(result = lr.predict(bow))










