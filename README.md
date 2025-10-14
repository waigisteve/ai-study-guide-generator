# 🎓 AI Study Guide Generator

An AI-powered Gradio app that generates detailed, structured study guides for any topic using OpenAI.

## Project contents
- app.py : Gradio + OpenAI app
- requirements.txt : dependencies
- README.md : this file

## Setup (local)
1. Create a .env in the project root with:
   OPENAI_API_KEY=sk-...
   HF_TOKEN=hf-...
   GITHUB_TOKEN=ghp-...

2. Install:
   pip install -r requirements.txt

3. Run:
   python app.py

## Deploy to Hugging Face Spaces
After pushing this repo to GitHub, deploy with:
    gradio deploy --space waigisteve/ai-study-guide-generator

Replace waigisteve and ai-study-guide-generator accordingly.
