Pré-requisitos:

1) Instalar Python 3.7 ou superior (https://www.python.org/downloads/);
2) Instalar o Flash (pip install flask)
3) Instalar o NLTK (pip install nltk)
4) Instalar o Psycopg2 (pip install psycopg2)
5) Instalar o textblob (pip install textblob)
6) Instalar o client MySQL (pip install mysql-connector-python)
7) Instalar o PyCountry (pip install pycountry)
8) Na primeira execução descomentar o código #nltk.download('punkt'), #nltk.download('stopwords'), #nltk.download('omw') e #nltk.download('wordnet')
9) Copiar a pasta WordNet para a pasta C:\Program Files (x86)\
10) Alterar a biblioteca Translate do TextBlob para não gerar erro ao não encontrar uma tradução para um determinado termo. Comente as linhas 84 e 85 do arquivo \venv\Lib\site-packages\textblob\translate.py 
