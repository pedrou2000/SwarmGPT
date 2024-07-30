from dotenv import load_dotenv
import os 
import constants
from typing import Any, Dict

def get_api_key(env_key_name, config_path=constants.ENV_FILE_PATH):
    # Check if the config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The configuration file {config_path} does not exist.")
    
    # Load the environment variables from config.env
    result = load_dotenv(dotenv_path=config_path)
    if not result:
        raise ValueError("The configuration file could not be loaded.")

    # Access the environment variables
    api_key = os.getenv(env_key_name)
    if not api_key:
        raise ValueError("The "+ env_key_name + " API key is not set in the configuration file.")
    
    return api_key

def get_openai_api_key(config_path=constants.ENV_FILE_PATH):
    return get_api_key("OPENAI_API_KEY", config_path=config_path)

def get_tavily_api_key(config_path=constants.ENV_FILE_PATH):
    return get_api_key("TAVILY_API_KEY", config_path=config_path)

def print_dict(d: Dict[str, Any], indent: int = 0) -> None:
    for k, v in d.items():
        print(f"{'    ' * indent}{k}:")
        if isinstance(v, dict):
            print_dict(v, indent + 1)
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    print_dict(item, indent + 1)
                else:
                    print(f"{'    ' * (indent + 1)}- {item}")
        elif isinstance(v, tuple):
            for item in v:
                if isinstance(item, dict):
                    print_dict(item, indent + 1)
                else:
                    print(f"{'    ' * (indent + 1)}- {item}")
        elif isinstance(v, str):
            lines = v.split('\n')
            for line in lines:
                print(f"{'    ' * (indent + 1)}{line}")

        elif isinstance(v, int) or isinstance(v, float):
            print(f"{'    ' * (indent + 1)}{v}")
        elif isinstance(v, bool):
            print(f"{'    ' * (indent + 1)}{v}")
        else:
            print(f"{'    ' * (indent + 1)}{v}")