'''
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv('DB.csv')
df = df[['Title', 'Slugs']]

# TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Slugs'].values.astype('U'))

# Calculate similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Create the recommendation model
recommendation_model = {
    'df': df,
    'tfidf': tfidf,
    'tfidf_matrix': tfidf_matrix,
    'cosine_sim': cosine_sim
}

# Save the model to disk
model_path = 'recommendation_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(recommendation_model, f)
'''