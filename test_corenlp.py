from nlplogic.corenlp import search_wikipedia, summarize_wikipedia, get_text_blob, get_phrases

def test_get_phrase():
    assert 'saint agur' in get_phrases("Saint Agur Blue")