import nltk
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

# Function for counting words in tweet
import math
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from collections import defaultdict

import math
from nltk.probability import FreqDist
from collections import defaultdict

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Создание DataFrame для примера
data = {
    'tweet_text': [['this', 'is', 'a', 'sample'], ['another', 'example', 'of', 'text']]
}
df = pd.DataFrame(data)

# Преобразование списков токенов в строки
df['text_joined'] = df['tweet_text'].apply(lambda x: ' '.join(x))

# Создание объекта TfidfVectorizer
vectorizer = TfidfVectorizer()

# Применение TfidfVectorizer к преобразованным строкам
tfidf_matrix = vectorizer.fit_transform(df['text_joined'])

# Просмотр результатов

def compute_tf_list(list):
    # >>> computating TF
    freq_list = FreqDist(list)
    tf = [word / len(list) for word in freq_list.values()]

    return tf