import tomli

with open("config/settings.toml", "rb") as file:
    toml_dict = tomli.load(file)
    print(toml_dict)