#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd

# Create a DataFrame from the provided data
data = pd.DataFrame({
    'name': [
        'Iron Man', 'The Incredible Hulk', 'Iron Man 2', 'Thor', 'Captain America: The First Avenger',
        'The Avengers', 'Iron Man 3', 'Thor: The Dark World', 'Captain America: The Winter Soldier',
        'Guardians of the Galaxy', 'Avengers: Age of Ultron', 'Ant-Man',
        'Captain America: Civil War', 'Doctor Strange', 'Guardians of the Galaxy Vol. 2',
        'Spider-Man: Homecoming', 'Thor: Ragnarok', 'Black Panther',
        'Avengers: Infinity War', 'Ant-Man and the Wasp', 'Captain Marvel', 'Avengers: Endgame',
        'Spider-Man: Far From Home'
    ],
    'year': [
        2008, 2008, 2010, 2011, 2011, 2012, 2013, 2013, 2014, 2014, 2015, 2015, 2016, 2016,
        2017, 2017, 2017, 2018, 2018, 2018, 2019, 2019, 2019
    ]
})

# Create a new column to assign clusters based on the specified year ranges
data['cluster'] = data['year'].apply(lambda x: '2008-2013' if 2008 <= x <= 2013 else '2014-2019')

# Function to search for movies by name and return year and cluster information
def search_by_movie(movie_name):
    movie = data[data['name'] == movie_name]
    if not movie.empty:
        year = movie.iloc[0]['year']
        cluster = movie.iloc[0]['cluster']
        return f"The movie '{movie_name}' was released in {year} and belongs to the {cluster} cluster."
    else:
        return f"The movie '{movie_name}' was not found in the dataset."

# Input the movie name
movie_input = input("Enter a Marvel movie name: ")
result = search_by_movie(movie_input)
print(result)


# In[42]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = pd.DataFrame({
    'name': [
        'Iron Man', 'The Incredible Hulk', 'Iron Man 2', 'Thor', 'Captain America: The First Avenger',
        'The Avengers', 'Iron Man 3', 'Thor: The Dark World', 'Captain America: The Winter Soldier',
        'Guardians of the Galaxy', 'Avengers: Age of Ultron', 'Ant-Man',
        'Captain America: Civil War', 'Doctor Strange', 'Guardians of the Galaxy Vol. 2',
        'Spider-Man: Homecoming', 'Thor: Ragnarok', 'Black Panther',
        'Avengers: Infinity War', 'Ant-Man and the Wasp', 'Captain Marvel', 'Avengers: Endgame',
        'Spider-Man: Far From Home'
    ],
    'year': [
        2008, 2008, 2010, 2011, 2011, 2012, 2013, 2013, 2014, 2014, 2015, 2015, 2016, 2016,
        2017, 2017, 2017, 2018, 2018, 2018, 2019, 2019, 2019
    ]
})
data['cluster'] = data['year'].apply(lambda x: 1 if 2008 <= x <= 2013 else 2)
def search_by_movie(movie_name):
    movie = data[data['name'] == movie_name]
    if not movie.empty:
        year = movie.iloc[0]['year']
        cluster = movie.iloc[0]['cluster']
        return f"The movie '{movie_name}' was released in {year} and belongs to Cluster {cluster}."
    else:
        return f"The movie '{movie_name}' was not found in the dataset."
movie_input = input("Enter a Marvel movie name: ")
result = search_by_movie(movie_input)
print(result)
plt.figure(figsize=(10, 6))
for cluster in [1, 2]:
    cluster_data = data[data['cluster'] == cluster]
    plt.scatter(cluster_data['year'], [cluster] * len(cluster_data), label=f'Cluster {cluster}', alpha=0.5)

plt.xlabel('Year')
plt.ylabel('Cluster')
plt.title('Marvel Movies Clustering by Release Year (Two Clusters)')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




