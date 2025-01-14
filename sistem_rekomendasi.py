# -*- coding: utf-8 -*-
"""Sistem_Rekomendasi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com
"""

#import library
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import hstack
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

#Membaca dan menampilkan data csv
dataRead = pd.read_csv("/content/Data_Netfilx.csv")
dataRead.head()

dataRead['content'] = dataRead['description'] + ' ' + dataRead['director'] + ' ' + dataRead['cast'] + ' ' + dataRead['listed_in']

#Vectorizer menggunakan TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(dataRead['description'])

# Menampilkan asil vektor
print(tfidf_matrix.toarray())

# Menghitung persamaan data
persamaan_data = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Menampilkan hasil dalam bentuk matriks
print(persamaan_data)

def rekomendasi(title, cosine_sim, dataRead):
    # Cari indeks film berdasarkan judul
    id = dataRead[dataRead['title'] == title].index[0]

    # Skor kesamaan untuk semua film
    similarity_scores = list(enumerate(cosine_sim[id]))

    # Urutkan berdasarkan skor kesamaan
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Ambil 3 film teratas (selain film yang dicari)
    similarity_scores = similarity_scores[1:4]
    movie_indices = [i[0] for i in similarity_scores]

    # Return judul film yang direkomendasikan
    return dataRead['title'].iloc[movie_indices]

# Contoh rekomendasi untuk 'Inception'
print(rekomendasi('Inception', persamaan_data, dataRead))