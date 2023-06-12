#Library Import and File Unloading
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Read dataset
movie_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.basics.tsv', sep='\t')
#saving title_basics.tsv
rating_df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/title.ratings.tsv', sep='\t') #untuk menyimpan title.ratings.tsv

#Cleaning table movie
print(movie_df.head()) #5 data teratas movie

#Check NULL Value
print(movie_df.isnull().sum())

#Analisis Kolom dengan data bernilai NULL
print(movie_df.loc[movie_df['primaryTitle'].isnull() & movie_df['originalTitle'].isnull()])
print(movie_df.loc[movie_df['genres'].isnull()])
#mengupdate movie_df dengan membuang data-data bernilai NULL
movie_df = movie_df.loc[movie_df['primaryTitle'].notnull() & movie_df['originalTitle'].notnull()]
movie_df = movie_df.loc[movie_df['genres'].notnull()]
#menampilkan jumlah data setelah data dengan nilai NULL dibuang
print(len(movie_df))

#mengubah nilai '\\N' pada startYear menjadi np.nan dan cast kolomnya menjadi float64
movie_df['startYear'] = movie_df['startYear'].replace('\\N', np.nan)
movie_df['startYear'] = movie_df['startYear'].astype('float64')
print(movie_df['startYear'].unique()[:5])
#mengubah nilai '\\N' pada endYear menjadi np.nan dan cast kolomnya menjadi float64
movie_df['endYear'] = movie_df['endYear'].replace('\\N', np.nan)
movie_df['endYear'] = movie_df['endYear'].astype('float64')
print(movie_df['endYear'].unique()[:5])

#mengubah nilai '\\N' pada runtimeMinutes menjadi np.nan dan cast kolomnya menjadi float64
movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].replace('\\N', np.nan)
movie_df['runtimeMinutes'] = movie_df['runtimeMinutes'].astype('float64')
print(movie_df['runtimeMinutes'].unique()[:5])

def transform_to_list(x):
    if ',' in x: 
    #ubah menjadi list apabila ada data pada kolom genre
        return x.split(',')
    else: 
    #jika tidak ada data, ubah menjadi list kosong
        return []

movie_df['genres'] = movie_df['genres'].apply(lambda x: transform_to_list(x))

#Cleaning table ratings
print(rating_df.head()) #Menampilkan 5 data teratas rating


#Joining table movie and table ratings
movie_rating_df = pd.merge(movie_df, rating_df, on='tconst', how='inner')
movie_rating_df = movie_rating_df.dropna(subset=['startYear', 'runtimeMinutes'])
print(movie_rating_df.head())#Tampilkan 5 data teratas
print(movie_rating_df.info())

#Building Simple Recommender System
C = movie_rating_df['averageRating'].mean() #find C value
print(C)
m = movie_rating_df['numVotes'].quantile(0.8) #find m value, numVotes >80% population, takin' 20% population
print(m)

def imdb_weighted_rating(df, var=0.8):
    v = df['numVotes']
    R = df['averageRating']
    C = df['averageRating'].mean()
    m = df['numVotes'].quantile(var)
    df['score'] = (v / (m + v)) * R + (m / (m + v)) * C
    return df['score']
    
imdb_weighted_rating(movie_rating_df)

def simple_recommender(df, top=100):
    df = df.loc[df['numVotes'] >= m]
    df = df.sort_values(by='score', ascending=False) #urutkan dari nilai tertinggi ke terendah
    
    #Ambil data 100 teratas
    df = df[:top]
    return df
    
#Ambil data 25 teratas     
# print(simple_recommender(movie_rating_df, top=25))

df = movie_rating_df.copy()

def user_prefer_recommender(df, ask_adult, ask_start_year, ask_genre, top=100):
    # ask_adult = yes/no
    if ask_adult.lower() == 'yes':
        df = df.loc[df['isAdult'] == 1]
    elif ask_adult.lower() == 'no':
        df = df.loc[df['isAdult'] == 0]

    # ask_start_year = numeric
    df = df.loc[df['startYear'] >= int(ask_start_year)]

    # ask_genre = 'all' atau yang lain
    if ask_genre.lower() == 'all':
        df = df
    else:
        def filter_genre(x):
            if ask_genre.lower() in str(x).lower():
                return True
            else:
                return False
        df = df.loc[df['genres'].apply(lambda x: filter_genre(x))]

    df = df.loc[df['numVotes'] >= m]  # Mengambil film dengan numVotes yang lebih besar atau sama dengan nilai m
    df = df.sort_values(by='score', ascending=False)

    # jika mengambil 100 teratas
    df = df[:top]
    return df

print(user_prefer_recommender(df, ask_adult='no', ask_start_year=2000, ask_genre='drama'))



