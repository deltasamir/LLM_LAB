from enum import Enum

class Weather_status(str,Enum):
    CLEAR_SKY = "Clear sky"
    PARTLY_CLOUDY = "Partly cloudy"
    CLOUDY = "Cloudy"
    OVERCAST = "Overcast"
    FOG = "Fog"
    MIST = "Mist"
    RAIN = "Rain"
    SHOWERS = "Showers"
    THUNDERSTORM ="Thunderstorm"
    DRIZZLE = "Drizzle"
    SNOW = "Snow"
    SLEET = "Sleet"
    HAIL = "Hail"
    WINDY = "Windy"
    DUST_STORM ="Dust storm"
    TROPICAL_STORM = "Tropical storm"
    HURRICANE = "Hurricane"
    BLIZZARD = "Blizzard"
    EXTREME_HEAT = "Extreme heat"
    EXTREME_COLD = "Extreme cold"
    
    
    