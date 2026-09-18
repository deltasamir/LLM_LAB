
weather_schemas = {
    "name":"wether",
    "strict":True,
    "schema":{
        "type":"object",
        "properties":{
            "city":{
                "type":"string",
                "description":"the name of the city extracted directly from the text eg:paris  "
            },
            "temperature":{
                "type":"number",
                "description":"the temperature motioned formatted as decimal (eg : 22.5) assume it's on celsius "
            }
        },
        "required":["city","temperature"],
        "additionalProperties":False
    }
}