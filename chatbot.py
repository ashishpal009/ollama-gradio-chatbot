import ollama
import gradio as gr

def llama_chatbot(message, history):
    response = ollama.generate(model='llama3.2:1b', prompt=message)['response']
    return response

# Launch the Gradio chat interface
gr.ChatInterface(llama_chatbot).launch(share=True)
