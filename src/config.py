import yaml

# Open config file to prevent cascading
# Use: from config import config in other files
with open("config.yml", "r") as f:
    config = yaml.safe_load(f)
