import tomli

with open("config/settings.toml", "rb") as file:
    config = tomli.load(file)
    print("ALL --> ", config)

# Accessing a specific section

config_database = config["database"]
print("DATABASE --> ", config_database)

ports_database = config_database["ports"]
print("PORTS --> ", ports_database)