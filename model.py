import pandas as pd
from sklearn.naive_bayes import GaussianNB
import joblib

def train_model():
    df = pd.read_csv('discount_data.csv')
    X = df[['price_ratio', 'days_since_change', 'seller_rating']]
    y = df['is_fake']
    
    model = GaussianNB()
    model.fit(X, y)
    
    joblib.dump(model, 'model.pkl')