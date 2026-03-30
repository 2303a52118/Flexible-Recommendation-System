
🚀 Flexible Recommendation System

A dynamic and customizable Recommendation System built using Python, Pandas, Scikit-learn, and Streamlit that generates personalized suggestions based on user behavior.

This system allows users to upload any dataset and automatically create recommendations using Collaborative Filtering.

🎯 Key Highlights
🔄 Works with ANY dataset (Movies, Products, etc.)                                                                                              
🧠 Uses User-Based Collaborative Filtering                                                                                                                        
⚡ Built with interactive UI using Streamlit                                                                                                                     
📊 Automatically detects:                                                                                                                                   
User column                                                                                                                                                        
Item column                                                                                                                                                    
Rating column                                                                                                                                               
🛠 Handles missing and inconsistent data
🔁 Falls back to popular recommendations if no personalized results
🧠 How It Works
1. Data Processing                                                                                                                                             
Upload CSV dataset
Automatically detects relevant columns
Cleans and preprocesses data
2. User-Item Matrix                                                                                                                            
Converts dataset into a matrix of users vs items
3. Similarity Calculation
Uses Cosine Similarity to find similar users
4. Recommendation Logic
Selects top similar users
Finds highly rated items
Removes already seen items
Generates final recommendations
⚙️ Tech Stack
Language: Python
Libraries:
Pandas
NumPy
Scikit-learn
Frontend/UI:
Streamlit


📂 Project Structure
Flexible-Recommendation-System/
│── app.py               # Streamlit application
│── recommender.py       # Recommendation logic
│── sample_data.csv      # Sample dataset (optional)
│── README.md            # Documentation



📊 Example Dataset Format
user_id	    product_id	rating
  1	         101        	5
  1	         102	        4
  2	         101	        4
  2	         103	        5
🎯 Features
✅ Personalized Recommendations

Recommendations based on behavior of similar users

✅ Flexible Input

Works with:

E-commerce datasets
Movie datasets (like MovieLens)
Any user-item-rating dataset
✅ Smart Fallback

If no recommendations found:
→ Displays top-rated popular items

🔍 Core Algorithm
User-Based Collaborative Filtering
Cosine Similarity

Improved UI with filters and search
- Built a flexible recommendation engine supporting dynamic datasets
- Implemented user similarity using cosine similarity
- Handles up to 5000+ user interactions efficiently
- Provides real-time personalized recommendations
