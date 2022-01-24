
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app
import dash_table


# --------------------- Packages

import re
import numpy as np
import pandas as pd
from pprint import pprint

from datetime import datetime

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# spacy for lemmatization
import spacy

# Plotting tools
import pyLDAvis
# import pyLDAvis.gensim  # Author: don't skip this
# pyLDAvis.gensim.prepare

# I think i need another one:
import pyLDAvis.gensim_models
import pyLDAvis.gensim_models as gensimvis

# Plots
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Enable logging for gensim - optional
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning)

# TF.IDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics.pairwise import cosine_distances
# NLTK Stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('dutch')
stop_words.extend(['tenlastelegging', 'hof', 'althans', 'tenlastegelegd', 'naan', 'verklaring', 'verklaren', 'benadelen', 'naam', 'aangeefster', 'aangever', 'aangev',
 'verbalisant', 'slachtoffer', 'rechtbank', 'uur', 'uren', 'weten', 'bestaan', 'waarheid', 'daarvoor', 'genaamd', 'maken', 'gaan', 'toverweging', 'aanzien', 'bewijs', 'feit', 
 'grond', 'staan', 'vaststellen', 'halen', 'vervolgens', 'nemen', 'aanhouden', 'bevinden', 'officier', 'justitie', 'overtuigen', 'bewijzen', 'maken', 'stellen', 'leggen', 'dienen', 
 'vrijspreken', 'daarnaast', 'bezigen', 'willen', 'gaan', 'vervolgens', 'raken', 'weten', 'proberen', 'echter', 'vraag', 'verdenken', 'vervatten', 'beslissing', 'hoger_beroep', 'verkort_vonni',
  'geacht', 'instellen', 'ander', 'zien', 'toebehoren', 'hoeveelheid', 'lijst_ii', 'bereiken'])


# ------------------------------------------- Data

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

# owner: shivp Kaggle. Source: https://data.mendeley.com/datasets
# dataset was modified. Original data: https://www.kaggle.com/shivkp/customer-behaviour

df18 = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/data_2018.csv'), index_col=0) 
df19 = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/data_2019.csv'), index_col=0) 
df20 = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/data_2020.csv'), index_col=0) 
df21 = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/data_2021.csv'), index_col=0) 

convert_dict = {'lemm': str,
                'year': str}
  
df18 = df18.astype(convert_dict)
df19 = df19.astype(convert_dict)
df20 = df20.astype(convert_dict)
df21 = df21.astype(convert_dict)

d = [df18, df19, df20, df21]

for i in d:
    test_list = []
    for j in i['lemm']:
        test_list.append(j.split())
    
    i['lemm_tok'] = test_list

print(df18.shape)
print(df19.shape)
print(df20.shape)
print(df21.shape)

tfidf18 = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/topidfs_2018.csv'), index_col=0) 
tfidf19 = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/topidfs_2019.csv'), index_col=0) 
tfidf20 = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/topidfs_2020.csv'), index_col=0) 
tfidf21 = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/topidfs_2021.csv'), index_col=0) 

top_idfs = [tfidf18, tfidf19, tfidf20, tfidf21]

i2w_df = pd.read_csv(DATA_PATH.joinpath('/Users/dj/Python - UvA/DSP/i2words_df.csv'), index_col=0) 


years = ['2018', '2019', '2020', '2021']

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])



# --------------------------------------------

layout = html.Div([
    html.H1('Video Games Sales', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='y1-dropdown', value='2018', clearable=False,
            options=[{'label': x, 'value': x} for x in years]
        ), className='six columns'),

        html.Div(dcc.Dropdown(
            id='y2-dropdown', value='2019', clearable=False,
            persistence=True, persistence_type='memory',
            options=[{'label': x, 'value': x} for x in years]
        ), className='six columns'),
    ], className='row'),

    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df18)
])





