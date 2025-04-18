#!/bin/bash
echo "Starting build process..."
python data_generator.py
python model.py

# Verify model creation
if [ -f "model.pkl" ]; then
    echo "✅ Model created successfully"
else
    echo "❌ Model creation failed!"
    exit 1
fi