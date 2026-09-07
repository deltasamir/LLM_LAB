import os
from dotenv import load_dotenv
from openai import OpenAI
from src.apps.LLM.config import client
from src.apps.schemas.schemas import Conversation

conversation = Conversation("you are wether specialist ")
#model_name
model_name :str = "ultron"
print(f"welcome to {model_name}:) ")
while True:
 #starting loop
 
  user_prompt = input("\n you :") 
  
  #checks if user want too exit the program
  
  if user_prompt.strip().lower() in ["exit","quit"]:
      print("see you soon ")
      break
  
  #user enter his input 
  user_input = conversation.add_message("user",user_prompt)
  
  response = client.chat.completions.create(
      model="openrouter/free",
      messages=conversation.get_messages(),
      temperature=0.7,
      max_tokens=300
  )

  reply = response.choices[0].message.content
  print(f"{model_name} : {reply}")