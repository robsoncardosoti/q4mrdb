from textblob import TextBlob
from nltk.corpus import wordnet as wn  #nltk.download('omw')

def detect_language(sentence):
    sentence = TextBlob(sentence)
    idiom = sentence.detect_language()
    return idiom

def pre_translation(sentence, idiom):
    sentence = TextBlob(sentence)
    translation = sentence.translate(to=idiom)
    return translation

def pos_translation(token, idiom):
    translation = []
    syn = wn.synsets(token, pos='n')[0].name()    #######  wn.synsets('dog', pos='v' or pos=wn.VERB)
    ln = [item.lower() for item in wn.synset(syn).lemma_names(idiom)]
    for term in ln:
        if term not in translation:
            translation[0] = [idiom.upper()] #[translated.append(term)]
            translation.append(term)
    return translation


####  Sample  ####
# sentence = TextBlob("What is the number of employees in the Computer Science department?")
# print(sentence.detect_language())
# print(sentence.translate(to='pt'))

