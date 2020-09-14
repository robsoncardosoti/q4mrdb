from flask import Flask, render_template, request, redirect, url_for
import nltk
from string import punctuation  #### REMOVE PONTUAÇÂO
from sqlFunctions import Aggregate, Order, Group, Compound
from nltk.tokenize import MWETokenizer  #### TOKENIZA MULTI-WORD
from nltk.corpus import wordnet as wn
import psycopg2  # !pip install psycopg2
from textblob import TextBlob
from tme import Tme

app = Flask(__name__)

class Query:
    def __init__(self, sentence):
        self.sentence = sentence

history = []


@app.route('/')
def home():
    return render_template('home.html', title='Query for Multilanguage Relational Databases (Q4MRD)', results=history)

@app.route('/search', methods=['POST',])
def search():
    history.clear()
    ####  USER QUERY ####
    history.append('CONSULTA INICIAL: ')
    sentence = request.form['sentence'].lower()  # A consulta inicial é convertida para LowerCase pois a lista de StopWords é somente minúsculas
    #acentuacao = unidecode.unidecode(sentence)  ### Remove acentuação
    history.append(sentence)
    term_value = sentence[sentence.find("'"):sentence.rfind("'") + 1]  ### Identifica a substring entre aspas simples
    ### Substitui os termos entre aspas simples pelo valor fixo 'term_value'
    if term_value != '':
        new_sentence = sentence.replace(term_value, 'term_value')
        print('Term Value: ', term_value)
    else:
        new_sentence = sentence
        print('Term Value Not Found!!!')

    '''for a in Aggregate():   ### Como "min" esta na sentenca "adMINistration" essa lógica não funciona
        if a in new_sentence:
            print(a)'''
    tokenizer = MWETokenizer(Compound(), separator='_')

    ####  1- QUERY SEGMENTATION (TOKENIZATION)  ####
    tokens = tokenizer.tokenize([p for p in nltk.word_tokenize(new_sentence) if p not in punctuation])  # REMOVE PONTUAÇÃO [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]
    history.append('SEGMENTAÇÃO DA CONSULTA: ')
    history.append(tokens)
    functions = tokens

    ####  2 - FUNCTIONS IDENTIFICATION    ####
    for t in functions:
        if t in Aggregate():
            aggregate = Aggregate()[t] + ''
            aggregate_function = aggregate + '(' + functions[functions.index(t) + 1] + ')'
            functions.remove(t)
            print('Aggregate Function: ', aggregate_function)
        elif t in Order():
            ordered = Order()[t] + ''  ### concatena com valor vazio para instanciar a variável caso o if não seja atendido.
            ordered_function = ordered + ' ' + functions[functions.index(t) + 1]
            functions.remove(t)
            print('Order By Function: ', ordered_function)
        elif t in Group():
            grouped = Group()[t]
            grouped_function = grouped + ' ' + functions[functions.index(t) + 1]
            functions.remove(t)
            print('Group By Function: ', grouped_function)
    history.append('IDENTIFICAÇÃO DE FUNÇÕES: ')
    history.append(functions)

    ####  3 - STOPWORDS REMOVAL ####
    stopword_function = [s for s in tokens if s not in nltk.corpus.stopwords.words('english')]  #### ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    history.append('REMOÇÃO DE STOPWORDS: ')
    history.append(stopword_function)

    ####  4 - RADICAL EXTRACTION (LEMMATIZATION) ####
    lemmatizer = nltk.WordNetLemmatizer()
    radical = [lemmatizer.lemmatize(l) for l in stopword_function]
    #morfema = [wn.morphy(m) for m in stopword_function]  ### USANDO WORDNET
    history.append('EXTRAÇÃO DO RADICAL: ')
    history.append(radical)

    ####  5 - QUERY EXPANSION  ####
    synonyms = []
    expanded_terms = []
    history.append('EXPANSÃO DA CONSULTA: ')
    for x in radical:
        for syn in wn.synsets(x, pos='n'):
            for l in syn.lemmas():
                if l.name() not in synonyms:
                    synonyms.append(l.name())
                    history.append(l.name())
                if l.name() not in x:
                    expanded_terms.append(l.name())

    # LANGUAGE IDENTIFICATION
#    conn = psycopg2.connect(host='127.0.0.1', port='5432', database='tme', user='tme', password='q4dbrm')
#    cur = conn.cursor()  # Open a cursor to perform database operations
#    cur.execute("SELECT DISTINCT(dc_language) FROM public.tme WHERE dispquery = 'True';")  # AND dc_language <> 'eng'  # Query the database and obtain data as Python objects
#    idiomas = [item[0] for item in cur.fetchall()]  # cur.fetchall()
    #print('Idiomas disponíveis: ', idiomas)
#    cur.close()  # Close communication with the database
#    conn.close()

    ####  6 - QUERY TRANSLATION - API GOOGLE  ####
    history.append('TRADUÇÃO DA CONSULTA (API GOOGLE): ')
    sent = ' '.join([e for e in radical])
    sentence = TextBlob(sent)
    token = sentence.words
    gtranslate = []
    for i in Tme.idiom():
        history.append(i.upper())
        gtranslate.append([i.upper()])
        if i == 'por':
            for e in token:
                gtranslate.append(e.translate(to='pt'))
                history.append(e.translate(to='pt'))
                # Criar tabela conversão https://pt.wikipedia.org/wiki/ISO_639

    ####  6 - QUERY TRANSLATION (OPEN MULTILINGUAL WORDNET) ####
    history.append('TRADUÇÃO DA CONSULTA (OPEN MULTILINGUAL WORDNET): ')
    translated = []
    translated.append('idiomas')
    for i in Tme.idiom():
        history.append(i.upper())
        translated.append([i.upper()])
        for qt in radical:
            syn = wn.synsets(qt)[0].name()  #######  wn.synsets('dog', pos='v' or pos=wn.VERB)
            ln = [item.lower() for item in wn.synset(syn).lemma_names(i)]
            # print(ln)
            for term in ln:
                if term not in translated:
                    translated[0] = [i.upper()]  # [translated.append(term)]
                    translated.append(term)
                    history.append(term)
        print(translated)

    return redirect(url_for('home'))


app.run(host='localhost', port=5000, debug=True)