#!pip install langid
#!pip install guess_language-spirit
#!pip install langdetect

import langid
from guess_language import guess_language
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 42

def check_language(text: str, language: str) -> dict:
    d = {"original_language": language}
    d["langid"] = langid.classify(text)[0]     #first model
    d["guess_language"] = guess_language(text) #second model
    try:                                       #third model
        d["langdetect"] = detect(text)
    except Exception:
        d["langdetect"] = "UNKNOWN"
        
    possible_languages = d.values()
    possible_languages = [i for i in possible_languages if i != "UNKNOWN"]
        
    if len(possible_languages) < 2:
        d["language_is_correct"] = -1 #-1 means the text is possibly nonsense

    elif len(possible_languages) == possible_languages.count(language):
        d["language_is_correct"] = 2 #2 means the language is definitely correct
    
    elif language in possible_languages:
        d["language_is_correct"] = 1 #1 means the language is possibly correct

    return d