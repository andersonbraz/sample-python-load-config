import yaml

with open("config/settings.yaml", "r") as file:
    config = yaml.safe_load(file)
    print("ALL --> ", config)

# Accessing a specific section
config_database = config[0]["database"]
print("DATABASE --> ", config_database)
# Accessing a specific section
ports_database = config_database["ports"]
print("PORTS --> ", ports_database)