import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.title("🚀 Flexible Recommendation System")

st.info("👉 Select 3 DIFFERENT columns: User, Item, and Rating")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    try:
        # ✅ Read CSV (auto handle MovieLens too)
        df = pd.read_csv(file)

        if len(df.columns) == 1:
            df = pd.read_csv(file, sep='::', engine='python')

    except:
        df = pd.read_csv(file, sep='::', engine='python')

    st.write("### 📊 Dataset Preview")
    st.dataframe(df.head())

    st.write("### ⚙️ Select Columns")

    # Auto-detect columns
    default_user = [col for col in df.columns if 'user' in col.lower()]
    default_item = [col for col in df.columns if 'movie' in col.lower() or 'item' in col.lower() or 'product' in col.lower()]
    default_rating = [col for col in df.columns if 'rating' in col.lower() or 'score' in col.lower()]

    user_col = st.selectbox(
        "Select User Column",
        df.columns,
        index=df.columns.get_loc(default_user[0]) if default_user else 0
    )

    item_col = st.selectbox(
        "Select Product/Item Column",
        df.columns,
        index=df.columns.get_loc(default_item[0]) if default_item else min(1, len(df.columns)-1)
    )

    rating_col = st.selectbox(
        "Select Rating Column",
        df.columns,
        index=df.columns.get_loc(default_rating[0]) if default_rating else min(2, len(df.columns)-1)
    )

    try:
        # Prevent duplicate selection
        if len({user_col, item_col, rating_col}) < 3:
            st.error("⚠️ Please select DIFFERENT columns")
            st.stop()

        # Rename
        data = df.rename(columns={
            user_col: 'user_id',
            item_col: 'product_id',
            rating_col: 'rating'
        })

        data = data[['user_id', 'product_id', 'rating']]

        # Clean
        data['rating'] = pd.to_numeric(data['rating'], errors='coerce')
        data = data.dropna().head(5000)

        # Matrix
        user_matrix = data.pivot_table(
            index='user_id',
            columns='product_id',
            values='rating'
        ).fillna(0)

        if user_matrix.shape[0] < 2:
            st.warning("Not enough users")
            st.stop()

        similarity = cosine_similarity(user_matrix)

        user_ids = user_matrix.index.tolist()
        selected_user = st.selectbox("Select User", user_ids)

        if st.button("Get Recommendations"):

            user_index = user_ids.index(selected_user)

            sim_scores = sorted(
                list(enumerate(similarity[user_index])),
                key=lambda x: x[1],
                reverse=True
            )

            similar_users = [i[0] for i in sim_scores[1:3]]

            recommended_products = set()

            for u in similar_users:
                user_ratings = user_matrix.iloc[u]
                liked = user_ratings[user_ratings >= user_ratings.mean()].index
                recommended_products.update(liked)

            seen = user_matrix.loc[selected_user]
            seen_items = seen[seen > 0].index

            final = list(recommended_products - set(seen_items))

            if not final:
                st.warning("No personalized recommendations. Showing popular items.")

                popular = data.groupby('product_id')['rating'].mean().sort_values(ascending=False)
                result = popular.head(5).reset_index()
                result.columns = ['Recommended Items', 'Score']
                st.dataframe(result)

            else:
                scores = data.groupby('product_id')['rating'].mean().reset_index()
                scores = scores[scores['product_id'].isin(final)]
                scores = scores.sort_values(by='rating', ascending=False)

                scores.columns = ['Recommended Items', 'Score']

                st.write("### 🎯 Recommended Items (Ranked)")
                st.dataframe(scores)

    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Upload any dataset to begin")