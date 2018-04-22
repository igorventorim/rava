import csv
import re
import nltk
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.feature_extraction.text import CountVectorizer

def __std_words__(string, blacklist=['maruipe', 'goiabeiras']):
    tokenizer = re.compile('\w+')
    tkn = tokenizer.findall(string)
    blacklist = blacklist + nltk.corpus.stopwords.words("portuguese")
    return " ".join([t for t in tkn if t not in blacklist])

db = []
with open("pratos.csv","r") as csv_:
    db = csv_.readlines()
db = [sample.split(";") for idx, sample in enumerate(db)]

db = db[1:]

for idsample, sample in enumerate(db):
    idx, text, freq = sample
    text = __std_words__(text.lower())
    db[idsample] = idx, text, freq

vectorizer = CountVectorizer(analyzer="char_wb", ngram_range=(4,8))
vcnt = vectorizer.fit_transform([d[1] for d in db])

features = vectorizer.get_feature_names()

query = ["carne"]
query = ["frango frito"]

vectorizer = CountVectorizer(analyzer="char_wb", ngram_range=(4,8), vocabulary=features)

query_vcnt = vectorizer.fit_transform(query)
print([ db[idx] for idx, dist in sorted([(ids, pairwise_distances(query_vcnt, s, metric="cosine")[0][0]) for ids, s in enumerate(vcnt)], key=lambda x:x[1]) if dist < 0.0001])