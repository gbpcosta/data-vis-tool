import pandas as pd
import nltk
import string
import re

from collections.abc import Iterable

nltk.download('stopwords')

PUNCTUATION_REGEX = re.compile('[%s]' % re.escape(string.punctuation))


def do_remove_stopwords(text, stopwords):
    if not isinstance(stopwords, Iterable):
        stopwords = nltk.corpus.stopwords.words('english')
    else:
        stopwords = [word.lower() for word in stopwords]

    text = ' '.join([word for word in nltk.tokenize.word_tokenize(text)
                     if word.lower() not in stopwords])
    return text


def do_replace_punctuation(text, punctuation):
    rep_str = ' '
    if isinstance(punctuation, str):
        rep_str = punctuation

    return PUNCTUATION_REGEX.sub(rep_str, text)


def preprocess_text(text, lowercase=False, remove_stopwords=False,
                    replace_punctuation=False, remove_punctuation=False,
                    replace_whitespaces=False,
                    tokenize=False):
    if lowercase:
        text = text.lower()

    if remove_stopwords:
        text = do_remove_stopwords(text, remove_stopwords)

    if replace_punctuation:
        text = do_replace_punctuation(text, replace_punctuation)

    if remove_punctuation:
        text = text.translate(str.maketrans('', '', string.punctuation))

    if replace_whitespaces:
        text = ' '.join(text.split())

    text = text.strip()

    return text
