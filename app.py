import gradio as gr
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_study_guide(topic):
    prompt = f'Create a detailed study guide for {topic} with sections, summaries, and key points.'
    response = openai.ChatCompletion.create(
        model='gpt-4-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a study guide assistant.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    return response.choices[0].message.content.strip()

iface = gr.Interface(
    fn=generate_study_guide,
    inputs='text',
    outputs='text',
    title='AI Study Guide Generator',
    description='Generate personalized study guides powered by OpenAI.'
)

if __name__ == '__main__':
    iface.launch()
