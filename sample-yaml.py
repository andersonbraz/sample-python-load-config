import yaml

with open("config/settings.yaml", "r") as file:
    prime_service = yaml.safe_load(file)
    print(prime_service)