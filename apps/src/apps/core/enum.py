from enum import Enum

class WeatherStatus(str,Enum):
    CLEARSKY = "Clear sky"
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
    DUSTSTORM ="Dust storm"
    TROPICALSTORM = "Tropical storm"
    HURRICANE = "Hurricane"
    BLIZZARD = "Blizzard"
    EXTREMEHEAT = "Extreme heat"
    EXTREMECOLD = "Extreme cold"
    
    
    