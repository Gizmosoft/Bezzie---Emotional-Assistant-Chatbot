### THIS SCRIPT IS USED TO TRAIN THE ML MODEL AND SAVE IT ###

import json as j
import pandas as pd
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, chi2
import pickle
import os

import json
json_file_path = "dataset/yesno.json"
with open(os.path.abspath(json_file_path), 'r') as j:
     contents = json.loads(j.read())

data = pd.DataFrame(contents)

X_train, X_test, y_train, y_test = train_test_split(data['response'], data.intent, test_size=0.2)

pipeline = Pipeline([('vect', TfidfVectorizer(ngram_range=(1, 2), stop_words="english", sublinear_tf=True)),
                     ('chi',  SelectKBest(chi2, k='all')),
                     ('clf', LogisticRegression(C=1.0, penalty='l2', max_iter=3000, dual=False, random_state=0,solver='liblinear'))])

model = pipeline.fit(X_train, y_train)
vectorizer = model.named_steps['vect']
chi = model.named_steps['chi']
clf = model.named_steps['clf']

feature_names = vectorizer.get_feature_names()
feature_names = [feature_names[i] for i in chi.get_support(indices=True)]
feature_names = np.asarray(feature_names)

# save the model to disk
filename = 'models/yesno.sav'
pickle.dump(model, open(filename, 'wb'))
