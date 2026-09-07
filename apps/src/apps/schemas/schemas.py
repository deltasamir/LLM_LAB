from openai import OpenAI

class Conversation:
    def __init__(self,system_prompt:str = "you are a helpful assistant "):
        self._messages = []
        if system_prompt:
            self.add_message("system",system_prompt)
        
    def add_message(self,role:str,content:str):
        self._messages.append({"role":role,"content":content})
        
    def get_messages(self):
        return self._messages