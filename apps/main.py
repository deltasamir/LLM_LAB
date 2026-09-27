import os
from typing import Any, cast
from dotenv import load_dotenv
from openai import OpenAI,APIConnectionError
import json

from src.apps.LLM.config import client
from src.apps.schemas.schemas import Conversation
from src.apps.schemas.json_schemas import weather_schemas
from src.apps.models.weather import Weather_data
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
   response = client.chat.completions.parse(
      model="openai/gpt-4o",
      messages=conversation.get_messages(),
      temperature=0.7,
      max_tokens=300,
      response_format= Weather_data,
   )
  
   reply = response.choices[0].message
   
   
   if reply.parsed is None:
            print(f"{model_name}: Unparseable response received.")
            continue
       
   weather_result: Weather_data = reply.parsed
   
   conversation.add_message("assistant", weather_result.model_dump_json())
   
   print(f"{model_name} :")
   print(f"Country : {weather_result.country_name}")
   print(f"City : {weather_result.city_name}")
   print(f"Temperature : {weather_result.temperature}")
   print(f"Weather : {weather_result.weather}")
   print(f"Humidity : {weather_result.humidity}")
   
       
  except APIConnectionError:
     print("\n Network Connection error")
     continue 
  except Exception as e:
      print(f"\n An error occurred : {e} ")