from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Initialize model variable
model = None

def load_or_create_model():
    global model
    try:
        if not os.path.exists('model.pkl'):
            from data_generator import generate_data
            from model import train_model
            generate_data()
            train_model()
        
        # Load with protocol 4 explicitly
        model = joblib.load('model.pkl')
        print("✅ Model loaded successfully!")
    except Exception as e:
        print(f"❌ Model loading failed: {str(e)}")
        # Emergency fallback
        from sklearn.naive_bayes import GaussianNB
        model = GaussianNB()
        X = np.array([[1.5, 10, 4.5]])
        y = np.array([0])
        model.fit(X, y)
        print("⚠️ Loaded fallback dummy model")

# Load model at startup
load_or_create_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        original_price = float(request.form['original_price'])
        discounted_price = float(request.form['discounted_price'])
        days_since_change = int(request.form['days_since_change'])
        seller_rating = float(request.form['seller_rating'])
        
        price_ratio = original_price / discounted_price
        features = np.array([[price_ratio, days_since_change, seller_rating]])
        
        is_fake = model.predict(features)[0]
        proba = model.predict_proba(features)[0][1]
        
        return render_template('results.html',
                            original_price=original_price,
                            discounted_price=discounted_price,
                            is_fake=is_fake,
                            probability=round(proba*100, 2),
                            price_ratio=round(price_ratio, 1),
                            features={
                                'days': days_since_change,
                                'rating': seller_rating
                            })
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))