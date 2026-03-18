import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, users_df, products_df):
        self.users = users_df
        self.products = products_df

    def prepare_data(self):
        self.user_matrix = self.users.pivot_table(
            index='user_id',
            columns='product_id',
            values='rating'
        ).fillna(0)

        self.similarity_matrix = cosine_similarity(self.user_matrix)

    def recommend(self, user_id):
        if user_id not in self.user_matrix.index:
            return pd.DataFrame()

        user_index = list(self.user_matrix.index).index(user_id)

        similarity_scores = list(enumerate(self.similarity_matrix[user_index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        similar_users = [i[0] for i in similarity_scores[1:3]]

        recommended_products = set()

        for sim_user in similar_users:
            user_products = self.user_matrix.iloc[sim_user]
            liked_products = user_products[user_products > 3].index
            recommended_products.update(liked_products)

        current_user_products = self.user_matrix.loc[user_id]
        seen = current_user_products[current_user_products > 0].index

        recommendations = list(recommended_products - set(seen))

        return self.products[self.products['product_id'].isin(recommendations)]