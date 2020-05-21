from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL  # pip install --only-binary :all: mysqlclient    #pip install flask_mysqldb
import numpy as np  # pip install numpy
import similarity as sim
import pandas as pd  # pip install pandas
import re
import MySQLdb
import psycopg2  # !pip install psycopg2
from sqlFunctions import SqlFunctions
import nltk  # pip install nltk
from tme import Dao
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
from string import punctuation  #### REMOVE PONTUAÇÂO
from nltk.tokenize import MWETokenizer  #### TOKENIZA MULTI-WORD
# !pip install unidecode
# import unidecode  ####   REMOVE ACENTOS

# import nltk
# nltk.download('wordnet')
from nltk.corpus import wordnet as wn
# nltk.download('omw') ## http://compling.hss.ntu.edu.sg/omw/ ###29 idiomas = ['als','arb','bul','cat','cmn','dan','ell','eng','eus','fas','fin','fra','glg','heb','hrv','ind','ita','jpn','nld','nno','nob','pol','por','qcn','slv','spa','swe','tha','zsm']
from translation import pre_translation, pos_translation

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "203501"
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)


class Query:
    def __init__(self, sentenca):
        self.sentenca = sentenca


lista = []


@app.route('/')
def principal():
    return render_template('home.html', titulo='Keyword Query in Multilanguage Relational Databases',
                           results=lista)


@app.route('/pesquisar', methods=['POST', ])
def pesquisar():
    lista.clear()
    ####  USER QUERY ####
    lista.append('Consulta Inicial: ')
    sentence = request.form[
        'sentenca'].lower()  # A consulta inicial é convertida para LowerCase pois a lista de StopWords é somente minúsculas
    # acentuacao = unidecode.unidecode(sentenca)  ### Remove acentuação
    lista.append(sentence)
    term_value = sentence[sentence.find("'") + 1:sentence.rfind("'")]  ### Identifica a substring entre aspas simples
    new_sentence = sentence.replace(term_value,
                                    'term_value')  ### Substitui os termos entre aspas simples pelo valor fixo 'term_value'
    ####  PRE-PROCESSING MODULE  ####
    ####  1 - QUERY SEGMENTATION (TOKENIZATION)  ####
    # ??????  usar "_" underline para palavras compostas  ????????
    tokenizer = MWETokenizer([("order", "by"), ("of", "each"), ("computer", "science"), ("how", "many")], separator='_')
    # tokens = nltk.word_tokenize(new_sentence)
    tokens = tokenizer.tokenize([p for p in nltk.word_tokenize(new_sentence) if p not in punctuation])
    # REMOVE PONTUAÇÃO
    # pontuacao = [p for p in tokens if p not in punctuation] #### [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]
    lista.append('Tokens: ')
    lista.append(tokens)
    #### POS TAG  ####
    # pos = nltk.pos_tag(tokens)
    # print(pos)

    ####  2 - FUNCTIONS IDENTIFICATION  ####
    # ???  FALTA ARMAZENAR A POSICAO ??????
    # funcoes = [f for f in pontuacao if f not in SqlFunctions()]
    # funcoes = [f for f in pontuacao if f in SqlFunctions()]
    # funcoes_removidas = [f for f in pontuacao if f not in SqlFunctions()]

    # posicao = [pontuacao.find(funcoes) + len(funcoes)]
    # print(posicao)
    # termos = (pontuacao[posicao + 1:].split(" ")[0])
    # print(termos)
    # print("SELECT {}({}) FROM".format(SqlFunctions()[funcoes], termos))

    # print('Funções: ', funcoes, 'Funções removidas: ', funcoes_removidas)
    '''for function in (SqlFunctions()):
        if function in sentenca:
            functions = [function]
            posicao = (sentenca.find(function) + len(function))
            termos = (sentenca[posicao + 1:].split(" ")[0])
            print("SELECT {}({}) FROM".format(SqlFunctions()[function], termos))
            # newquery = [query]
            # newquery.remove(function)
            # print(type(query))
            # newquery = query.del(functions)
            if len(functions) == 0:
                print("nao encontrada")'''

    ####  3 - STOPWORDS REMOVAL ####
    stopword_function = [s for s in tokens if s not in nltk.corpus.stopwords.words(
        'english')]  #### ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    funcoes_removidas = [f for f in stopword_function if f not in SqlFunctions()]

    for f in stopword_function:
        if f in SqlFunctions():
            termos_funcoes = [f]
            funcoes = SqlFunctions().get(f)
            print(funcoes)
            posicao = stopword_function.index(f)
            termos = stopword_function[(posicao + 1)]
            # print("SELECT {}({}) FROM".format(funcoes, termos))

    lista.append('Funções: ')
    lista.append(funcoes)

    lista.append('StopWords: ')
    lista.append(stopword_function)

    ####  4 - RADICAL EXTRACTION (LEMMATIZATION) ####
    lemmatizer = nltk.WordNetLemmatizer()
    radical = [lemmatizer.lemmatize(l) for l in funcoes_removidas]
    morfema = [wn.morphy(m) for m in funcoes_removidas]  ### USANDO WORDNET
    lista.append('Lemma: ')
    lista.append(radical)

    ####  5 - QUERY EXPANSION  ####
    # query_expansion = radical
    lista.append('Query Expansion: ')
    '''for synset in wn.synsets("department"):
        for lemma in synset.lemmas():
            if lemma.name() not in radical:
                lista.append([lemma.name()])
                query_expansion.append(lemma.name())
    print('QueryExpansion: ', query_expansion)
'''
    synonyms = []
    expanded_terms = []

    for x in radical:
        for syn in wn.synsets(x):
            for l in syn.lemmas():
                if l.name() not in synonyms:
                    synonyms.append(l.name())
                    lista.append(l.name())
                if l.name() not in x:
                    expanded_terms.append(l.name())
    # print('Termos expandidos: ', expanded_terms)
    ####  TRANSLATION MODULE  ####

    ####  6 - LANGUAGE IDENTIFICATION  ####
    conn = psycopg2.connect(host='127.0.0.1', port='5432', database='tme', user='tme', password='q4dbrm')
    cur = conn.cursor()  # Open a cursor to perform database operations
    cur.execute(
        "SELECT DISTINCT(dc_language) FROM public.tme WHERE dispquery = 'True' AND dc_language <> 'eng';")  # Query the database and obtain data as Python objects
    idiomas = [item[0] for item in cur.fetchall()]  # cur.fetchall()
    cur.close()  # Close communication with the database
    conn.close()

    ####  7 - QUERY TRANSLATION  ####
    lista.append('QUERY TRANSLATION: ')
    translated = []
    for i in idiomas:
        lista.append(i.upper())
        translated.append(i.upper())
        for qt in radical:
            syn = wn.synsets(qt)[0].name()  #######  wn.synsets('dog', pos='v' or pos=wn.VERB)
            ln = [item.lower() for item in wn.synset(syn).lemma_names(i)]
            # print(ln)
            for term in ln:
                if term not in translated:
                    translated[0] = [i.upper()]  # [translated.append(term)]
                    translated.append(term)
                    lista.append(term)
        # print(translated)

    ####  DATABASE MODULE  ####

    ####  8 - RELEVANT DATABASE IDENTIFICATION  ####
    conn = psycopg2.connect(host='127.0.0.1', port='5432', database='tme', user='tme', password='q4dbrm')
    cur = conn.cursor()  # Open a cursor to perform database operations
    cur.execute("SELECT dc_description, dc_subject, dc_title, dc_identifier FROM public.tme "
                "WHERE dispquery = 'True'")
    # "AND dc_language= XXX"
    describe_db = cur.fetchall()
    cur.close()  # Close communication with the database
    conn.close()
    count = 0
    #### CONTA QUANTIDADE DE OCORRENCIAS DO TERMO NA TME
    relevant_db = {}
    for w in describe_db:
        dc_description = w[0]
        dc_subject = w[1]
        dc_title = w[2]
        dc_identifier = w[3]
        for y in w:
            for q in synonyms:
                if re.search(q, y, re.IGNORECASE):
                    count = count + 1
                    # print(q, "Foi encontrado em: ", y, "do banco :", dc_identifier)
        # rank_db.append([dc_identifier, count])
        relevant_db.update({dc_identifier: count})
        count = 0
    rank_db = [item for item in sorted(relevant_db, key=relevant_db.get, reverse=True) if relevant_db[item] != 0]

    lista.append('DB RELEVANT: ')
    lista.append(relevant_db)

    lista.append('RANK DB: ')
    lista.append(rank_db)

    print("\n\n0. User Query: ", sentenca,
          '\n1. Query Segmentation: ', tokens,
          '\n2. StopWords Removal: ', stopword_function,
          '\n3. Functions Identification: ', funcoes_removidas,
          '\n4. Radical Extraction: ', radical,
          '\n5. Query Expansion: ', synonyms,
          '\n6. Language Identification: ', idiomas,
          '\n7. Query Translation: ', translated,
          '\n8. Relevant DB: ', relevant_db,
          '\n9. Rank DB: ', rank_db)
    ####  9 - DATABASE RANKING  ####

    ####  10 - SCHEMA EXTRACTION  ####
    pgsql = "SELECT table_name, column_name, udt_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_schema NOT IN ('pg_catalog', 'information_schema')"
    mysql = "SELECT COLUMN_NAME AS column_name, DATA_TYPE AS column_type FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '${this.config.database}'"

    ####  MAPPING MODULE  ####
    ####  11 - INTRINSIC WEIGHT CALCULATION  ####
    data = np.array([['', 'col1', 'col2'], ['Row1', 1, 2]])
    print(data)
    # print('Levenshtein: ', sim.levenshtein('laço', 'aço'))
    # print('jaccard: ', sim.jaccard('laço', 'aço'))
    # print('cosine: ', sim.cosine('laço', 'aço'))
    print('avg_sim', sim.avg('laço', 'aço'))

    ####  12 - GENERATION SETTINGS ####

    ####  13 - GENERATION INTERPRETATIONS  ####

    #### QUERY MODULE  ####
    ####  14 - RESULTS RANKING  ####

    ####  15 - QUERY EXECUTION  ####
    '''conn = psycopg2.connect(host='127.0.0.1', port='5432', database='tme', user='tme', password='q4dbrm')
    cur = conn.cursor()
    cur.execute("SELECT dc_title, dc_type, url, provider, loginbd, passwordbd FROM public.tme "
                "WHERE dc_title = XXXXXXXXXX")
    cur.fetchall()
    cur.close()
    conn.close()'''

    return redirect(url_for('principal'))


app.run(host='localhost', port=5000, debug=True)
