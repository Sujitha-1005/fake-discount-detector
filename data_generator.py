import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    
    # Real discounts (class 0)
    real_data = {
        'price_ratio': np.random.uniform(1.1, 2.5, 500),  # 10%-150% discounts
        'days_since_change': np.random.randint(1, 30, 500),
        'seller_rating': np.random.uniform(3.5, 5, 500),
        'is_fake': 0
    }
    
    # Fake discounts (class 1)
    fake_data = {
        'price_ratio': np.random.uniform(3, 10, 500),  # 70%-90% "discounts"
        'days_since_change': np.random.randint(1, 3, 500),  # Recently changed
        'seller_rating': np.random.uniform(1, 3.5, 500),
        'is_fake': 1
    }
    
    df = pd.concat([pd.DataFrame(real_data), pd.DataFrame(fake_data)])
    df.to_csv('discount_data.csv', index=False)