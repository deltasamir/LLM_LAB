from pydantic import BaseModel,Field
from apps.core.enum import Weather_status 
class Weather_data(BaseModel):
    contry_name:str = Field(
        description="the name of the contry eg (france , algeria , usa ....)"
    )
    city_name:str = Field(
        description="the name of the city eg paris algers new york ..."
    )
    temperature:float = Field(
        description="the temperature on degree celcus"
    )
    weather : Weather_status = Field(
        description=" give the weather status eg rain ....."
    )
    humidity : float = Field(
        description="give the humidity percentage eg : 30%,80% ...."
    )
    
