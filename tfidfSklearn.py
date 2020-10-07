import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import *

get60sLyrics()
get70sLyrics()
get80sLyrics()
get90sLyrics()
get00sLyrics()
get10sLyrics()

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([clean60s, clean70s, clean80s, clean90s, clean00s, clean10s])
feature_names = vectorizer.get_feature_names()
dense = vectors.todense()
denselist = dense.tolist()
df = pd.DataFrame(denselist, columns=feature_names)