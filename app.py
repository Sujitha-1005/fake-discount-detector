from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from sklearn.naive_bayes import GaussianNB
import numpy as np
import joblib
import os
 
app = Flask(__name__)
 
 # Generate synthetic data if no model exists
if not os.path.exists('model.pkl'):
     from data_generator import generate_data
     from model import train_model
     generate_data()
     train_model()
 
model = joblib.load('model.pkl')
 
@app.route('/')
def home():
     return render_template('index.html')
 
@app.route('/detect', methods=['POST'])
def detect():
     # Get form data
     original_price = float(request.form['original_price'])
     discounted_price = float(request.form['discounted_price'])
     days_since_change = int(request.form['days_since_change'])
     seller_rating = float(request.form['seller_rating'])
     
     # Calculate features
     price_ratio = original_price / discounted_price
     features = np.array([[price_ratio, days_since_change, seller_rating]])
     
     # Predict
     is_fake = model.predict(features)[0]
     proba = model.predict_proba(features)[0][1]  # Probability of being fake
     
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
 
if __name__ == '__main__':
     app.run(debug=True)