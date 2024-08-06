from nlplogic.corenlp import get_phrases


def test_get_phrase():
    assert "saint agur" in get_phrases("Saint Agur Blue")
