import pandas as pd
import spacy
import functools
import logging

logger = logging.getLogger(__name__)

# python -m spacy download en_core_web_lg
@functools.lru_cache(maxsize=1)
def load_or_get_spacy_model():
    logger.info('Loading GloVe model (Spacy)')
    return spacy.load('en_core_web_lg', disable=["tagger", "parser", "ner"])


def get_glove_vector_doc(text):
    logger.info('Extracting GloVe Vector (average)')
    nlp = load_or_get_spacy_model()
    return nlp(text).vector


def get_batch_glove_vector_doc(texts):
    logger.info('Extracting GloVe Vector (average) - batch')
    nlp = load_or_get_spacy_model()
    return [tt.vector for tt in nlp.pipe(texts)]


def get_glove_vector_token(text):
    logger.info('Extracting GloVe Vector (per word)')
    nlp = load_or_get_spacy_model()
    tokens = nlp(text)

    descriptors = []
    for tk in tokens:
        descriptors.append({'token': tk,
                            'vector': tk.vector,
                            'vector_norm': tk.vector_norm,
                            'has_vector': tk.has_vector,
                            'is_oov': tk.is_oov})

    return pd.DataFrame(descriptors)


# python -m spacy download en_trf_bertbaseuncased_lg
@functools.lru_cache(maxsize=1)
def load_or_get_bert_model():
    logger.info('Loading BERT model (Spacy)')
    return spacy.load("en_trf_bertbaseuncased_lg")


def get_bert_vector_doc(text):
    logger.info('Extracting BERT Vector (average)')
    nlp = load_or_get_bert_model()
    return nlp(text).vector


def get_batch_bert_vector_doc(texts):
    logger.info('Extracting BERT Vector (average) - batch')
    nlp = load_or_get_bert_model()
    return [tt.vector for tt in nlp.pipe(texts)]


def get_bert_vector_token(text):
    logger.info('Extracting BERT Vector (per word)')
    nlp = load_or_get_bert_model()
    tokens = nlp(text)

    descriptors = []
    for tk in tokens:
        descriptors.append({'token': tk,
                            'vector': tk.vector,
                            'vector_norm': tk.vector_norm,
                            'has_vector': tk.has_vector,
                            'is_oov': tk.is_oov})

    return pd.DataFrame(descriptors)
