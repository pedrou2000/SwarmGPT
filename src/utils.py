from dotenv import load_dotenv
import os 
import constants

def get_api_key(env_key_name, config_path=constants.ENV_FILE_PATH):
    # Check if the config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The configuration file {config_path} does not exist.")
    
    # Load the environment variables from config.env
    load_dotenv(config_path)

    # Access the environment variables
    api_key = os.getenv(env_key_name)
    if not api_key:
        raise ValueError("The "+ env_key_name + " API key is not set in the configuration file.")
    
    return api_key

def get_openai_api_key(config_path=constants.ENV_FILE_PATH):
    return get_api_key("OPENAI_API_KEY", config_path=config_path)

def get_tavily_api_key(config_path=constants.ENV_FILE_PATH):
    return get_api_key("TAVILY_API_KEY", config_path=config_path)
