import os
from typing import Any, cast
from dotenv import load_dotenv
from openai import OpenAI,APIConnectionError
import json

from src.apps.LLM.config import client
from src.apps.schemas.schemas import Conversation
from src.apps.schemas.json_schemas import weather_schemas
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
  try:
   response = client.chat.completions.create(
      model="openai/gpt-4o",
      messages=conversation.get_messages(),
      temperature=0.7,
      max_tokens=300,
      response_format=cast(Any, {
          "type": "json_schema",
          "json_schema": weather_schemas
        })
   )
  
   reply = response.choices[0].message.content or ""
  
   conversation.add_message("assistant",reply)
  
   weather_data = json.loads(reply)
  
   print(f"{model_name} : ",json.dumps(weather_data,indent=2))
  except APIConnectionError:
     print("\n Network Connection error")
     continue 