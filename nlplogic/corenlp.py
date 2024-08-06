from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search Wikipedia"""
    print(f"searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize Wikipedia"""
    print(f"finding summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """getting textblob object and returns"""

    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """find wiki name and return phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
