import text_preprocessing


def test_preprocess_text():
    text = 'The Quick Brown Fox Jumped Over the Lazy dog.'
    assert text_preprocessing.preprocess_text(text, lowercase=True) == 'the quick brown fox jumped over the lazy dog.'

    text = 'The Quick Brown Fox Jumped Over. The Lazy dog.'
    assert text_preprocessing.preprocess_text(text, stopwords=True) == 'Quick Brown Fox Jumped . Lazy dog .'

    text = 'The Quick Brown Fox Jumped Over. The Lazy dog.'
    assert text_preprocessing.preprocess_text(text, stopwords=['dog', 'fox']) == 'The Quick Brown Jumped Over . The Lazy .'

    text = 'The Quick Brown Fox, Jumped Over! - The Lazy dog.'
    assert text_preprocessing.preprocess_text(text, replace_punctuation=True) == 'The Quick Brown Fox  Jumped Over    The Lazy dog'

    text = 'The Quick Brown Fox, Jumped Over! - The Lazy dog.'
    assert text_preprocessing.preprocess_text(text, remove_punctuation=True) == 'The Quick Brown Fox Jumped Over  The Lazy dog'
