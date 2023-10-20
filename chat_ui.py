import gradio as gr
from chatbot import Chatbot


chatbot = Chatbot()
demo = gr.ChatInterface(chatbot.chat)


if __name__ == "__main__":
    demo.launch()
