# AI Study Guide Generator

An AI-powered app that generates personalized study guides using OpenAI and Gradio.

## Features
- Generates study guides for any topic
- Uses OpenAI GPT models
- Interactive Gradio web interface
- Deployable on Hugging Face Spaces

## How to Run Locally
Run these commands in your terminal:
pip install -r requirements.txt
python app.py

## Deploy to Hugging Face
1. Push the repo to GitHub.
2. Create a Space on Hugging Face.
3. Add a Secret named OPENAI_API_KEY with your API key.
4. Deploy using:
gradio deploy --space waigisteve/ai-study-guide-generator
