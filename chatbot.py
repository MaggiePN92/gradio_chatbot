import openai
from dotenv import load_dotenv
import os
load_dotenv()


class Chatbot:
    def __init__(self, model = "gpt-3.5-turbo") -> None:
        self.api_key = openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model_list = openai.Model.list()
        self.avail_mods = self.list_avail_models()
        assert model in self.avail_mods, f"Model called {model} not available."
        self.model = model
        self.prompt = self.set_prompt()

    def set_prompt(self, instruction_prompt = None):
        if not instruction_prompt:
            instruction_prompt = "You are a helpful assistant."
        messages = [
            {"role": "system", "content": instruction_prompt}
        ]
        return messages

    def list_avail_models(self):
        avail_mods = []
        for model in self.model_list["data"]:
            avail_mods.append(model["root"])
        return avail_mods 
    
    def chat(self, message, history):
        context = self.prompt
        # old_messages = [[user_message, bot_message], ...] 
        for old_messages in history:
            context.append({"role":"user", "content":old_messages[0]})
            context.append({"role":"system", "content":old_messages[1]})
        # adding the newest msg to the context 
        context.append({"role":"user", "content":message})

        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=context
        )
        return completion["choices"][0]["message"]["content"]

if __name__ == "__main__":
    cb = Chatbot()
    print(cb.chat("Hello", []))
