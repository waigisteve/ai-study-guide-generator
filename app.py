import gradio as gr
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_study_guide(topic: str) -> str:
    if not topic:
        return "⚠️ Please provide a topic."

    prompt = f"Create a detailed, structured study guide for the topic: {topic}\nInclude overview, key concepts, examples, and action steps."

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=800,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error contacting OpenAI API: {str(e)}"

with gr.Blocks() as demo:
    gr.Markdown("# AI Study Guide Generator")
    topic = gr.Textbox(label="Enter a study topic", placeholder="e.g., PostgreSQL indexing")
    output = gr.Textbox(label="Generated Study Guide", lines=20)
    btn = gr.Button("Generate Study Guide")
    btn.click(generate_study_guide, inputs=topic, outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.getenv('PORT', 7860)))
