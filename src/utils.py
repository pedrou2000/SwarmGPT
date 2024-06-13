from dotenv import load_dotenv
import os 
import constants

def read_api_key(config_path=constants.ENV_FILE_PATH):
    # Check if the config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"The configuration file {config_path} does not exist.")
    
    # Load the environment variables from config.env
    load_dotenv(config_path)

    # Access the environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("The OpenAI API key is not set in the configuration file.")
    
    return openai_api_key
