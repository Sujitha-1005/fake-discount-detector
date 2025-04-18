#!/bin/bash
set -e  # Exit on error

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Generating data ==="
python data_generator.py

echo "=== Training model ==="
python model.py

echo "=== Verification ==="
if [ -f "model.pkl" ]; then
    echo "✅ Model verification passed"
    python -c "import joblib; print('Model type:', type(joblib.load('model.pkl')))"
else
    echo "❌ Model file missing!"
    exit 1
fi