import pandas as pd
from sklearn.naive_bayes import GaussianNB
import joblib

def train_model():
    try:
        df = pd.read_csv('discount_data.csv')
        X = df[['price_ratio', 'days_since_change', 'seller_rating']]
        y = df['is_fake']
        
        model = GaussianNB()
        model.fit(X, y)
        
        # Ensure protocol 4 is used
        joblib.dump(model, 'model.pkl', protocol=4)
        print("✅ Model trained and saved with protocol 4")
    except Exception as e:
        print(f"❌ Model training failed: {str(e)}")
        raise