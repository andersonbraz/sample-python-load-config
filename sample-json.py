import json

with open('config/settings.json', 'r') as file:
    config = json.load(file)
    print("ALL --> ", config)
    
# Accessing a specific section
config_database = config[0]["database"]
print("DATABASE --> ", config_database)
# Accessing a specific section
ports_database = config_database["ports"]
print("PORTS --> ", ports_database)