import nltk
from nltk.corpus import stopwords
import string
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,confusion_matrix

nltk.download('stopwords')

csv_path = 'docs.csv'
docs = pd.read_csv(csv_path)
#docs = docs.rename(columns={'v1': 'descripcion','v2': 'CPV'})
docs.head()
docs.groupby('CPV').describe()

docs_train, docs_test = train_test_split(docs,test_size=0.3,random_state=42)
docs_train.to_csv('train.csv',index=False)
docs_test.to_csv('test.csv',index=False)


