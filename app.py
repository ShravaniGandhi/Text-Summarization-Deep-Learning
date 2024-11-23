from flask import Flask, render_template, request
import tensorflow as tf
from keras.models import load_model
from tensorflow.keras.models import load_model
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained models
model_with_attention = load_model('model_with_attention.h5')
model_without_attention = load_model('model_without_attention.h5')

# Function to summarize the text (dummy function for now)
def summarize_text(text, model):
    # Implement your text summarization logic
    # For simplicity, let's just use a placeholder summary.
    # Replace this with your model's prediction function
    return text[:100]  # Dummy implementation - first 100 characters as summary

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    model_type = 'with_attention'  # Default to model with attention
    if request.method == 'POST':
        input_text = request.form['input_text']
        if 'with_attention' in request.form:
            model_type = 'with_attention'
            summary = summarize_text(input_text, model_with_attention)  # Get the summary using model with attention
        elif 'without_attention' in request.form:
            model_type = 'without_attention'
            summary = summarize_text(input_text, model_without_attention)  # Get the summary using model without attention
    return render_template('index.html', summary=summary, model_type=model_type)

if __name__ == '__main__':
    app.run(debug=True)
